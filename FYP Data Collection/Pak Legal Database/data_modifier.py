import json

input_path = r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Pak Legal Database\data_output.json"

output_path = r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Pak Legal Database"

with open(input_path, 'r') as f:
    data = json.load(f)

for item in data:
    if 'Summary' in item:
        item['Summary'] = item['Summary'].replace('Case Summary:', '')
    if 'Issue Type' in item:
        item['Issue Type'] = item['Issue Type'].replace('Category :', '').replace('Category:', '')
    if 'Court' in item:
        item['Court'] = item['Court'].replace('Jurisdiction:', '')
    if 'Judge Name' in item:
        item['Judge Name'] = item['Judge Name'].replace('Judge:', '')

with open(rf'{output_path}\data_updated.json', 'w') as f:
    json.dump(data, f, indent=4)
