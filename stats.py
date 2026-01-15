from rich.console import Console
from rich.table import Table
from rich import box


def print_fuel_eco(total_liters, total_fuel_cost, avg_price_per_liter, avg_fuel_eco):
    # render fuel statistics table
    fuel_stats = Table(title="Fuel statistics", box=box.SIMPLE_HEAD)

    fuel_stats.add_column("Total fuel consumption", justify="center", style="cyan", no_wrap=True)
    fuel_stats.add_column("Total fuel cost (CZK)", justify="center", style="cyan", no_wrap=True)
    fuel_stats.add_column("Average price per liter (CZK)", justify="center", style="cyan", no_wrap=True)
    fuel_stats.add_column("Average fuel economy", justify="center", style="cyan", no_wrap=True)

    fuel_stats.add_row(str(total_liters), str(total_fuel_cost), str(avg_price_per_liter), str(avg_fuel_eco))

    console = Console()
    console.print(fuel_stats)


def show_fuel_stats(data):
    if not data["fuel"]:
        print("No fuel entries yet.")
        return

    total_liters = round(sum(entry["liters"] for entry in data["fuel"]), 2)

    if total_liters == 0:
        print("Total liters is 0, cannot compute averages.")
        return

    total_fuel_cost = round(sum(entry["cost"] for entry in data["fuel"]), 2)

    avg_price_per_liter = round(total_fuel_cost / total_liters, 2)

    sorted_by_mileage = sorted(data["fuel"], key=lambda x: x["mileage"])

    if len(sorted_by_mileage) < 2:
        print("Not enough fuel entries to compute fuel economy.\n")
        print_fuel_eco(total_liters, total_fuel_cost, avg_price_per_liter, "N/A")
        return

    economies = []
    for i in range(1, len(sorted_by_mileage)):
        prev_entry = sorted_by_mileage[i - 1]
        curr_entry = sorted_by_mileage[i]

        distance = curr_entry["mileage"] - prev_entry["mileage"]
        liters = curr_entry["liters"]

        if liters > 0 and distance > 0:
            economy = distance / liters
            economies.append(economy)

    if not economies:
        print("Cannot compute fuel economy. Not enough entries.\n")
        print_fuel_eco(total_liters, total_fuel_cost, avg_price_per_liter, "N/A")
        return

    avg_fuel_economy = round(sum(economies) / len(economies), 2)

    print_fuel_eco(total_liters, total_fuel_cost, avg_price_per_liter, avg_fuel_economy)

def show_maintenance_stats(data):
    if not data["maintenance"]:
        print("No maintenance entries yet.")
        return

    total_maintenance_cost = round(sum(entry["cost"] for entry in data["maintenance"]), 2)

    total_entries = len(data["maintenance"])

    avg_cost_per_entry = round(total_maintenance_cost / total_entries, 2)


    # render maintenance statistics table
    maintenance_stats = Table(title="Maintenance statistics", box=box.SIMPLE_HEAD)

    maintenance_stats.add_column("Total entries", justify="center", style="cyan", no_wrap=True)
    maintenance_stats.add_column("Total Maintenance Cost (CZK)", justify="center", style="cyan", no_wrap=True)
    maintenance_stats.add_column("Avg. Cost per Entry (CZK)", justify="center", style="cyan", no_wrap=True)

    maintenance_stats.add_row(str(total_entries), str(total_maintenance_cost), str(avg_cost_per_entry))

    console = Console()
    console.print(maintenance_stats)    
