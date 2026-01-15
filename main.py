from data_io import load_data, save_data
from entries import add_maintenance_entry, add_fuel_entry, maintenance_history, fuel_history
from stats import show_fuel_stats, show_maintenance_stats

def main():
    data = load_data()

    while True:
        print("\nCar Maintenance Tracker")
        print("1) Add maintenance")
        print("2) Add fuel")
        print("3) View maintenance history")
        print("4) View fuel history")
        print("5) View statistics")
        print("0) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_maintenance_entry(data)
            save_data(data)
            print("New maintenance entry saved.")
        elif choice == "2":
            add_fuel_entry(data)
            save_data(data)
            print("New fuel entry saved.")
        elif choice == "3":
            print("")
            maintenance_history(data)
        elif choice == "4":
            print("")
            fuel_history(data)
        elif choice == "5":
            print("")
            show_fuel_stats(data)
            print("")
            show_maintenance_stats(data)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
