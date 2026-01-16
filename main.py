from data_io import load_data, save_data
from entries import add_maintenance_entry, add_fuel_entry, maintenance_history, fuel_history, delete_entry
from stats import show_fuel_stats, show_maintenance_stats
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    data = load_data()

    while True:
        clear_screen()

        print("\nCar Maintenance Tracker\n")
        print("1) Add maintenance")
        print("2) Add fuel")
        print("3) View maintenance history")
        print("4) View fuel history")
        print("5) View statistics")
        print("6) Delete maintenance entry")
        print("7) Delete fuel entry")
        print("0) Exit")

        choice = input("\nChoose an option: ").strip()

        print("")

        if choice == "1":
            add_maintenance_entry(data)
            save_data(data)
        elif choice == "2":
            add_fuel_entry(data)
            save_data(data)
        elif choice == "3":
            maintenance_history(data)
        elif choice == "4":
            fuel_history(data)
        elif choice == "5":
            show_fuel_stats(data)
            show_maintenance_stats(data)
        elif choice == "6":
            delete_entry(data, "maintenance")
            save_data(data)
        elif choice == "7":
            delete_entry(data, "fuel")
            save_data(data)
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice, please try again.")
        
        # wait before clearing the screen
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
