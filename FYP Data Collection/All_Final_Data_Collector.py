import json
import os

# Directory containing your JSON files
directory = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON'

# List to hold all dictionaries
merged_data = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='latin1') as f:
            data = json.load(f)
            if isinstance(data, list):
                merged_data.extend(data)

# Save the merged data to a new JSON file
with open(r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\merged_data.json', 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, indent=4)
