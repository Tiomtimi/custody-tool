# Digital Forensics Custody Tool

A beginner-friendly Python tool that records and verifies file integrity,
the same principle used in digital forensics to prove evidence has not been tampered with.

## Features
- Hashes every file in a folder with SHA-256
- Records size, last-modified time, scan time, and examiner name
- Saves everything to a custody log (`custody_log.csv`)
- Verifies later and flags files that are OK, MODIFIED, MISSING, or NEW
- Saves a timestamped verification report

## Usage
1. Create the baseline log:
   python hasher.py
   (enter the folder path, then the examiner name)
2. Verify later:
   python verify.py
   (enter the same folder path)

## Requirements
Python 3.8+. No external libraries needed.

## Limitations
- The custody log itself is not protected. Someone with access could edit it.
- Only compares content hashes, not deeper file system metadata.

## Author
Fawzy, cybersecurity student focusing on digital forensics.