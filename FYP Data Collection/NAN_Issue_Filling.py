import json

def fill_empty_fields(data):
    for dictionary in data:
        if not dictionary.get("Issue Type") or dictionary.get("Issue Type") == "nan" or dictionary.get("Issue Type") == "": 
            dictionary["Issue Type"] = "No Issue Type Found."
            
    return data


with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\Final Data - Editing.json", "r") as file:
    data = json.load(file)
    
updated_data = fill_empty_fields(data)


with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\Final Data - Editing.json", "w") as file:
    json.dump(updated_data, file, indent=4)
    
print("Fields updated successfully.")