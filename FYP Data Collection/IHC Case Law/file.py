import json
import re

# Load your JSON file
with open(r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\IHC Case Law\file.json', 'r') as f:
    data = json.load(f)

# Define a regex pattern to remove content within parentheses
pattern = re.compile(r'\s*\(.*?\)\s*')

# Iterate through each dictionary and modify the "Summary" attribute
for entry in data:
    if "Summary" in entry:
        entry["Summary"] = pattern.sub('', entry["Summary"]).strip()

# Save the modified data back to a JSON file
with open(r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\IHC Case Law\modified_file.json', 'w') as f:
    json.dump(data, f, indent=4)
