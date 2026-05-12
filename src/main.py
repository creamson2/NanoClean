import os
import shutil

def clear_temp():
    temp_dirs = [
        "/tmp",
        "/var/tmp",
        os.path.expanduser("~/.cache")
    ]

    for directory in temp_dirs:
        if os.path.exists(directory):
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                try:
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    else:
                        shutil.rmtree(item_path)
                except Exception as e:
                    print(f"Could not remove {item_path}: {e}")

def main():
    print("🧼 NanoClean is running...")
    clear_temp()
    print("✨ Cleaning complete!")

if __name__ == "__main__":
    main()

