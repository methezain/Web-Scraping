import json
import random
from datetime import datetime, timedelta

def generate_random_date():
    # Generate a random date between 2022-01-01 and 2024-12-31
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%d.%m.%Y") 

def fill_nan_dates(data):
    for dictionary in data:
        if dictionary.get("Date Filed") == "nan" or dictionary.get("Date Filed") == "Date not found" or not dictionary.get("Date Filed"):
            dictionary["Date Filed"] = generate_random_date()

    return data

# Load your JSON file
with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\All_Final_Data,.json", "r") as file:
    data = json.load(file)

# Fill 'nan' values with random dates
updated_data = fill_nan_dates(data)

# Write the updated JSON file back
with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\All_dates.json", "w") as file:
    json.dump(updated_data, file, indent=4)

print("Dates updated successfully.")
