# file_processing.py
from pathlib import Path

def scan_folder(folder):
    p = Path(folder)
    if not p.exists():
        print("Folder does not exist.")
        return

    for file in p.rglob("*"):
        print(f"{file} — {file.stat().st_size} bytes")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    scan_folder(folder)