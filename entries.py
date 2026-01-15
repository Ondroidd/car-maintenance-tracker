from rich.console import Console
from rich.table import Table
from rich import box
from datetime import datetime
import json

def render_history(data, kind, columns):
    # render fuel/maintenance entry table
    table = Table(title=f"{kind} history", box=box.SIMPLE_HEAD)
    for col in columns:
        table.add_column(col, justify="center", style="cyan", no_wrap=True)
    for entry in data:
        row = [str(entry[col]) for col in columns]
        table.add_row(*row)

    console = Console()
    console.print(table)

def maintenance_history(data):
    if not data["maintenance"]:
        print("No maintenance entries yet.")
    else:
        cols = ["date", "mileage", "service_type", "cost", "notes"]
        render_history(data["maintenance"], "Maintenance", cols)


def fuel_history(data):
    if not data["fuel"]:
        print("No fuel entries yet.")
    else:
        cols = ["date", "mileage", "liters", "cost", "price_per_liter"]
        render_history(data["fuel"], "Fuel", cols)


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
