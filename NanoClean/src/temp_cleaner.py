import os
import shutil
import time

def clean_temp():
    print("\nCleaning temporary files...\n")
    time.sleep(1)

    temp_path = os.getenv("TEMP")

    if not temp_path:
        print("Could not locate the Temp folder.")
        input("\nPress Enter to return to the menu...")
        return

    deleted = 0
    skipped = 0

    for root, dirs, files in os.walk(temp_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                deleted += 1
            except:
                skipped += 1

        for folder in dirs:
            folder_path = os.path.join(root, folder)
            try:
                shutil.rmtree(folder_path)
                deleted += 1
            except:
                skipped += 1

    print(f"Deleted items: {deleted}")
    print(f"Skipped (in use/locked): {skipped}")
    print("\nTemp cleaning complete.")
    input("\nPress Enter to return to the menu...")
