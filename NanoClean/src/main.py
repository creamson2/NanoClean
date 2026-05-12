from scanner import run_scan
from duplicate_finder import find_duplicates
from temp_cleaner import clean_temp
from log_manager import show_logs
from ui import clear_screen

def main_menu():
    while True:
        clear_screen()
        print("=== NanoClean Main Menu ===")
        print("1. Run System Scan")
        print("2. Find Duplicate Files")
        print("3. Clean Temporary Files")
        print("4. View Logs")
        print("5. Exit")
        
        choice = input("\nChoose an option: ")

        if choice == "1":
            run_scan()
        elif choice == "2":
            find_duplicates()
        elif choice == "3":
            clean_temp()
        elif choice == "4":
            show_logs()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            input("Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
