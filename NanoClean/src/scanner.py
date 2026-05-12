import time

def run_scan():
    print("\nStarting system scan...\n")
    time.sleep(1)

    fake_items = [
        "Checking system files...",
        "Scanning temporary folders...",
        "Analyzing disk usage...",
        "Looking for suspicious files...",
        "Finalizing scan..."
    ]

    for item in fake_items:
        print(item)
        time.sleep(0.8)

    print("\nScan complete! No threats found.\n")
    input("Press Enter to return to the menu...")
