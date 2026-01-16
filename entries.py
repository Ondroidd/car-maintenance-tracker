from rich.console import Console
from rich.table import Table
from rich import box
from datetime import datetime


def render_confirmation(entry, kind):
    # render fuel/maintenance entry before save/delete
    if kind == "maintenance":
        columns = ["date", "mileage", "service_type", "cost", "notes"]
    elif kind == "fuel":
        columns = ["date", "mileage", "liters", "cost", "price_per_liter"]

    table = Table(box=box.SIMPLE_HEAD)
    for col in columns:
        table.add_column(col, justify="center", style="cyan", no_wrap=True)
    row = [str(entry[col]) for col in columns]
    table.add_row(*row)

    console = Console()
    console.print(table)


def render_history(data, kind, columns):
    # render fuel/maintenance entry table
    table = Table(title=f"{kind} history", box=box.SIMPLE_HEAD, row_styles=["", "dim"])
    for col in columns:
        table.add_column(col, justify="center", style="cyan", no_wrap=True)
    for entry in data:
        row = [str(entry[col]) for col in columns]
        table.add_row(*row)

    console = Console()
    console.print(table)


def maintenance_history(data):
    if not data["maintenance"]:
        print("\nNo maintenance entries yet.")
    else:
        cols = ["date", "mileage", "service_type", "cost", "notes"]
        sorted_data = sorted(data["maintenance"], key=lambda x: x["date"])
        render_history(sorted_data, "Maintenance", cols)


def fuel_history(data):
    if not data["fuel"]:
        print("\nNo fuel entries yet.")
    else:
        cols = ["date", "mileage", "liters", "cost", "price_per_liter"]
        sorted_data = sorted(data["fuel"], key=lambda x: x["date"])
        render_history(sorted_data, "Fuel", cols)


def add_maintenance_entry(data):
    maintenance_entry = {}

    # Date
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD) (or 'q' to cancel): ").strip()
            if date_str.lower() == "q":
                print("\nEntry creation canceled.")
                return
            datetime.strptime(date_str, "%Y-%m-%d")  # Validate format
            maintenance_entry["date"] = date_str
            break
        except ValueError:
            print("\nPlease enter date in YYYY-MM-DD format.")

    # Mileage
    while True:
        try:
            mileage = input("Enter mileage (or 'q' to cancel): ").strip()
            if mileage.lower() == "q":
                print("\nEntry creation canceled.")
                return
            mileage = int(mileage)
            if mileage < 0:
                print("\nMileage cannot be negative. Please enter 0 or greater.")
                continue
            maintenance_entry["mileage"] = mileage
            break
        except ValueError:
            print("\nPlease enter a whole number for mileage (0 or greater).")

    # Service type
    while True:
        service_type = input("Enter service type (or 'q' to cancel): ").strip()
        if service_type.lower() == "q":
            print("\nEntry creation canceled.")
            return
        if service_type:
            maintenance_entry["service_type"] = service_type
            break
        print("\nService type cannot be empty.")

    # Cost
    while True:
        try:
            cost = input("Enter cost (or 'q' to cancel): ").strip()
            if cost.lower() == "q":
                print("\nEntry creation canceled.")
                return
            cost = float(cost)
            if cost < 0:
                print("\nCost cannot be negative. Please enter 0 or greater.")
                continue
            maintenance_entry["cost"] = cost
            break
        except ValueError:
            print("\nPlease enter a valid number for cost.")

    # Notes
    notes = input("Enter notes (optional) (or 'q' to cancel): ").strip()
    if notes.lower() == "q":
        print("\nEntry creation canceled.")
        return
    maintenance_entry["notes"] = notes if notes else None

    # confirmation before saving new entry
    print("\nYou entered:")
    render_confirmation(maintenance_entry, "maintenance")

    confirm = input("\nSave this entry? (Y/n): ").strip().lower()
    if confirm not in ("", "y"):
        print("\nEntry discarded.")
        return

    print("\nNew maintenance entry saved.")
    data["maintenance"].append(maintenance_entry)


def add_fuel_entry(data):
    fuel_entry = {}

    # Date
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD) (or 'q' to cancel): ").strip()
            if date_str.lower() == "q":
                print("\nEntry creation canceled.")
                return
            datetime.strptime(date_str, "%Y-%m-%d")  # Validate format
            fuel_entry["date"] = date_str
            break
        except ValueError:
            print("\nPlease enter date in YYYY-MM-DD format.")

    # Mileage
    while True:
        try:
            mileage = input("Enter mileage (or 'q' to cancel): ").strip()
            if mileage.lower() == "q":
                print("\nEntry creation canceled.")
                return
            mileage = int(mileage)
            if mileage < 0:
                print("\nMileage cannot be negative. Please enter 0 or greater.")
                continue
            fuel_entry["mileage"] = mileage
            break
        except ValueError:
            print("\nPlease enter a whole number for mileage (0 or greater).")

    # Liters
    while True:
        try:
            liters = input("Enter liters (or 'q' to cancel): ").strip()
            if liters.lower() == "q":
                print("\nEntry creation canceled.")
                return
            liters = float(liters)
            if liters <= 0:
                print("\nLiters must be greater than 0.")
                continue
            fuel_entry["liters"] = liters
            break
        except ValueError:
            print("\nPlease enter a valid number for liters.")

    # Cost
    while True:
        try:
            cost = input("Enter cost (or 'q' to cancel): ").strip()
            if cost.lower() == "q":
                print("\nEntry creation canceled.")
                return
            cost = float(cost)
            if cost < 0:
                print("\nCost cannot be negative. Please enter 0 or greater.")
                continue
            fuel_entry["cost"] = cost
            break
        except ValueError:
            print("\nPlease enter a valid number for cost.")

    # Price per liter
    fuel_entry["price_per_liter"] = round(cost / liters, 2)

    # confirmation before saving new entry
    print("\nYou entered:")
    render_confirmation(fuel_entry, "fuel")

    confirm = input("\nSave this entry? (Y/n): ").strip().lower()
    if confirm not in ("", "y"):
        print("\nEntry discarded.")
        return

    print("\nNew fuel entry saved.")
    data["fuel"].append(fuel_entry)


def delete_entry(data, kind):
    entries = data[kind]

    if not entries:
        print("\nThere are no entries to delete.")
        return

    for idx, entry in enumerate(entries, start=1):
        print(f"{idx}) {entry['date']} @ {entry['mileage']} - ...")
    
    while True:
        choice = input("\nEnter the number of the entry to delete (or 'q' to cancel): ").strip()
        if choice.lower() == "q":
            print("\nEntry deletion canceled.")
            return
        try:
            choice_num = int(choice)
            if not (1 <= choice_num <= len(entries)):
                print("\nInvalid entry number.")
                continue
            
            index = choice_num - 1 # convert back to 0-based idx

            # confirmation before deleting an entry
            print(f"\nYou have chosen {kind} entry:")
            render_confirmation(entries[index], kind)

            confirm = input("\nDelete this entry? (Y/n): ").strip().lower()
            if confirm not in ("", "y"):
                print("\nEntry deletion canceled.")
                return

            entries.pop(index)
            print("\nEntry deletion successful.")
            return 
        except ValueError:
            print("\nPlease enter a number from the list.")
