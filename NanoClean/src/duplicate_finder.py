import os
import hashlib
import time

def hash_file(path):
    """Generate a hash for a file to detect duplicates."""
    hasher = hashlib.md5()
    try:
        with open(path, "rb") as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except:
        return None

def find_duplicates():
    print("\nScanning for duplicate files...\n")
    time.sleep(1)

    search_path = os.path.expanduser("~")  # User home directory
    file_hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(search_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = hash_file(full_path)

            if file_hash:
                if file_hash in file_hashes:
                    duplicates.append(full_path)
                else:
                    file_hashes[file_hash] = full_path

    if duplicates:
        print("Duplicate files found:\n")
        for dup in duplicates:
            print(dup)
    else:
        print("No duplicate files found.")

    input("\nPress Enter to return to the menu...")
