import json
import random

names = [
    "Ahmed", "Aisha", "Fatima", "Ali", "Hassan", "Zainab", "Omar", "Maryam","Yusuf", "Sara", "Khadija", "Ibrahim", "Noor", "Mohammad", "Amina", "Bilal","Layla", "Ismail", "Hana", "Mustafa", "Rania", "Khalid", "Samira", "Mariam","Zaid", "Rashid", "Nadia", "Suleiman", "Asma", "Amir", "Sumaya", "Riyad","Anisa", "Junaid", "Nour", "Tariq", "Muna", "Hamza", "Yasmin", "Faisal"
]


def fill_empty_fields(data):
    for dictionary in data:
        if not dictionary.get("Client Name") or dictionary.get("Client Name") == "Client name not found" or dictionary.get("Client Name") == 'nan' or dictionary.get("Client Name") == "nna": 
            dictionary["Client Name"] = random.choice(names)
            
    return data


with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\Final Data - Editing.json", "r") as file:
    data = json.load(file)
updated_data = fill_empty_fields(data)


with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\Final Data - Editing.json", "w") as file:
    json.dump(updated_data, file, indent=4)
    
print("Fields updated successfully.")