from datetime import datetime
import json
import os


DATA_FILE = "data.json"


def load_data(filename=DATA_FILE):
    if not os.path.exists(filename):
        return {
            "maintenance": [],
            "fuel": []
        }

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data, filename=DATA_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_maintenance_entry(data):
    maintenance_entry = {}
    
    # Date
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD): ")
            datetime.strptime(date_str, "%Y-%m-%d")  # Validate format
            maintenance_entry["date"] = date_str
            break
        except ValueError:
            print("Please enter date in YYYY-MM-DD format.")
    
    # Mileage
    while True:
        try:
            mileage = int(input("Enter mileage: "))
            if mileage < 0:
                print("Mileage cannot be negative. Please enter 0 or greater.")
                continue
            maintenance_entry["mileage"] = mileage
            break
        except ValueError:
            print("Please enter a whole number for mileage (0 or greater).")
    
    # Service type
    while True:
        service_type = input("Enter service type: ").strip()
        if service_type:
            maintenance_entry["service_type"] = service_type
            break
        print("Service type cannot be empty.")
    
    # Cost
    while True:
        try:
            cost = float(input("Enter cost: "))
            if cost < 0:
                print("Cost cannot be negative. Please enter 0 or greater.")
                continue
            maintenance_entry["cost"] = cost
            break
        except ValueError:
            print("Please enter a valid number for cost.")
    
    # Notes
    notes = input("Enter notes (optional): ").strip()
    maintenance_entry["notes"] = notes if notes else None
    
    data["maintenance"].append(maintenance_entry)


def add_fuel_entry(data):
    fuel_entry = {}

    # Date
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD): ")
            datetime.strptime(date_str, "%Y-%m-%d")  # Validate format
            fuel_entry["date"] = date_str
            break
        except ValueError:
            print("Please enter date in YYYY-MM-DD format.")

    # Mileage
    while True:
        try:
            mileage = int(input("Enter mileage: "))
            if mileage < 0:
                print("Mileage cannot be negative. Please enter 0 or greater.")
                continue
            fuel_entry["mileage"] = mileage
            break
        except ValueError:
            print("Please enter a whole number for mileage (0 or greater).")

    # Liters
    while True:
        try:
            liters = float(input("Enter liters: "))
            if liters <= 0:
                print("Liters must be greater than 0.")
                continue
            fuel_entry["liters"] = liters
            break
        except ValueError:
            print("Please enter a valid number for liters.")

    # Cost
    while True:
        try:
            cost = float(input("Enter cost: "))
            if cost < 0:
                print("Cost cannot be negative. Please enter 0 or greater.")
                continue
            fuel_entry["cost"] = cost
            break
        except ValueError:
            print("Please enter a valid number for cost.")

    # Price per liter
    fuel_entry["price_per_liter"] = round(cost / liters, 2)

    data["fuel"].append(fuel_entry)


def main():
    data = load_data()

    add_fuel_entry(data)

    save_data(data)

    print(data)


if __name__ == "__main__":
    main()
