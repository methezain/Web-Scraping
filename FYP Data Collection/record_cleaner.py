import json
import re

def clean_dict(d):
    for key, value in d.items():
        if isinstance(value, str):
            value = re.sub(r'[\n\t\f]', '', value)
            value = re.sub(r'\s+', ' ', value).strip()
            value = value.encode('ascii', 'ignore').decode('ascii')
            d[key] = value
        elif isinstance(value, dict):
            clean_dict(value)
    return d

input_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\ALL_Final_Data.json'
output_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\cleaned_data.json'

with open(input_path, 'r') as file:
    data = json.load(file)

cleaned_data = [clean_dict(record) for record in data]

with open(output_path, 'w') as file:
    json.dump(cleaned_data, file, indent=4)
