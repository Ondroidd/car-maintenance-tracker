# Car Maintenance Tracker

A simple command-line application to track car maintenance and fuel usage.  
Data is stored in a JSON file and basic statistics are computed from history.

## Features

- Add maintenance entries
  - Date, mileage, service type, cost, notes
  - Input validation and ability to cancel
  - Confirmation before saving

- Add fuel entries
  - Date, mileage, liters, cost
  - Automatically calculates price per liter
  - Input validation and ability to cancel
  - Confirmation before saving

- View history
  - Maintenance history table
  - Fuel history table
  - Uses [`rich`](https://github.com/Textualize/rich) for nicely formatted tables

- View statistics
  - Fuel:
    - total liters
    - total fuel cost
    - average price per liter
    - average fuel economy (km/l), when enough data is available
  - Maintenance:
    - total number of entries
    - total maintenance cost
    - average cost per entry

- Manage entries
  - Delete maintenance entries
  - Delete fuel entries
  - Confirmation before deletion

## Requirements

- Python 3.10+
- Dependencies:
  - `rich`

Install dependencies:

```bash
pip install rich
```

## Usage

Clone the repo and run:

```bash
python main.py
```

You’ll see a menu like:
```
Car Maintenance Tracker
1) Add maintenance
2) Add fuel
3) View maintenance history
4) View fuel history
5) View statistics
6) Delete maintenance entry
7) Delete fuel entry
0) Exit
```
Data is stored in data.json in the project directory.
If data.json does not exist, it is created automatically with empty maintenance and fuel lists.

Data format (data.json):
```
{
  "maintenance": [
    {
      "date": "2024-01-14",
      "mileage": 123456,
      "service_type": "oil change",
      "cost": 799.0,
      "notes": "Used synthetic oil"
    }
  ],
  "fuel": [
    {
      "date": "2024-01-15",
      "mileage": 123800,
      "liters": 45.0,
      "cost": 60.0,
      "price_per_liter": 1.33
    }
  ]
}
