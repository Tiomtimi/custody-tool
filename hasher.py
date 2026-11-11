import hashlib
import os
import csv
import datetime

LOG_FILE = "custody_log.csv"

def hash_file(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def file_details(path):
    size = os.path.getsize(path)
    modified = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    return size, modified

folder = input("Enter folder path: ")
if not os.path.isdir(folder):
    print("Error: that folder does not exist:", folder)
    raise SystemExit
examiner = input("Examiner name: ")
scan_time = datetime.datetime.now()

with open(LOG_FILE, "w", newline="") as log:
    writer = csv.writer(log)
    writer.writerow(["Scan time", "Examiner", "File", "Size (bytes)", "Last modified", "SHA-256"])

    for root, dirs, files in os.walk(folder):
        for name in files:
            if name == LOG_FILE:
                continue
            path = os.path.join(root, name)
            size, modified = file_details(path)
            writer.writerow([scan_time, examiner, path, size, modified, hash_file(path)])
            print("Logged:", path)

print("Done. Log saved to", LOG_FILE)