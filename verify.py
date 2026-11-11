import hashlib
import os
import csv
import datetime

LOG_FILE = "custody_log.csv"
REPORT_FILE = "verification_report.txt"

def hash_file(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

if not os.path.exists(LOG_FILE):
    print("Error: no custody log found. Run hasher.py first.")
    raise SystemExit

folder = input("Enter folder path to verify: ")
if not os.path.isdir(folder):
    print("Error: that folder does not exist:", folder)
    raise SystemExit

lines = []
logged_paths = set()
intact = 0
problems = 0

with open(LOG_FILE, "r", newline="") as log:
    reader = csv.DictReader(log)
    for row in reader:
        path = row["File"]
        original_hash = row["SHA-256"]
        logged_paths.add(path)

        if not os.path.exists(path):
            lines.append("MISSING : " + path)
            problems += 1
        elif hash_file(path) != original_hash:
            lines.append("MODIFIED: " + path)
            problems += 1
        else:
            lines.append("OK      : " + path)
            intact += 1

for root, dirs, files in os.walk(folder):
    for name in files:
        if name in (LOG_FILE, REPORT_FILE):
            continue
        path = os.path.join(root, name)
        if path not in logged_paths:
            lines.append("NEW     : " + path)
            problems += 1

lines.append("-" * 40)
lines.append(f"{intact} file(s) intact, {problems} problem(s)")

header = f"Verification report - {datetime.datetime.now()}"
report_text = header + "\n" + "\n".join(lines) + "\n"

print(report_text)

with open(REPORT_FILE, "w", encoding="utf-8") as report:
    report.write(report_text)