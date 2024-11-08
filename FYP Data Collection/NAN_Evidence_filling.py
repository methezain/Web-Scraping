import json

def fill_empty_fields(data):
    for dictionary in data:
        if not dictionary.get("Evidence") or dictionary.get("Evidence") == "nan" or dictionary.get("Evidence") == "": 
            dictionary["Evidence"] = "No Evidence Found."
        
        if not dictionary.get("Witnesses") or dictionary.get("Witnesses") == "nan" or dictionary.get("Witnesses") == "": 
            dictionary["Witnesses"] = "No witness listed."
        
        if not dictionary.get("Legal Precedents") or dictionary.get("Legal Precedents") == "nan" or dictionary.get("Legal Precedents") == "": 
            dictionary["Legal Precedents"] = "No Legal Precedents Found." 
            
        if not dictionary.get("Outcome") or dictionary.get("Outcome") == "nan" or dictionary.get("Outcome") == "": 
            dictionary["Outcome"] = "No Outcomes yet." 
        
        if not dictionary.get("Appeal") or dictionary.get("Appeal") == "nan" or dictionary.get("Appeal") == "": 
            dictionary["Appeal"] = "No Appeal Found." 
        
        if not dictionary.get("Summary") or dictionary.get("Summary") == "nan" or dictionary.get("Summary") == "": 
            dictionary["Summary"] = "No Summary Found for this case."
            
    return data


with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\Final Data - Editing.json", "r") as file:
    data = json.load(file)
    
updated_data = fill_empty_fields(data)


with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\Final Data - Editing.json", "w") as file:
    json.dump(updated_data, file, indent=4)
    
print("Fields updated successfully.")