import json
import random

judges = [
    'TARIQ MEHMOOD JAHANGIRI', 'AAMER FAROOQ', 'BABAR SATTAR', 'MOHSIN AKHTAR KAYANI', 'MIANGUL HASSAN AURANGZEB','Sayyed Mazahar Ali Akbar Naqvi', 'Jawad Hassan', 'Maqbool Baqar','Muzamil Akhtar Shabir', 'Asif Saeed Khan Khosa', 'QAZI MUHAMMAD AMIN AHMED', 'Shujaat Ali Khan', 'Muhammad Azim Khan Afridi','Ch. Abdul Aziz', 'Abdul Hameed Baloch', 'Mirza Viqas Rauf'
]
def fill_empty_fields(data):
    for dictionary in data:
        if not dictionary.get("Judge Name") or dictionary.get("Judge Name") == "nan" or dictionary.get("Judge Name") == "" or dictionary.get("Judge Name") == 'judge name not found' or dictionary.get("Judge Name") == "(Pvt.)" or dictionary.get("Judge Name") == "(hereinafter referred to as 'the Constitution')" or dictionary.get("Judge Name") == "(West)" or dictionary.get("Judge Name") == "(WEST)" or dictionary.get("Judge Name") == "(i)" or dictionary.get("Judge Name") == "(1)" or dictionary.get("Judge Name") == "(01)" or dictionary.get("Judge Name") == "(02)" or dictionary.get("Judge Name") == "(03)" or dictionary.get("Judge Name") == "(04)" or dictionary.get("Judge Name") == "(05)" or dictionary.get("Judge Name") == "(06)" or dictionary.get("Judge Name") == "(07)" or dictionary.get("Judge Name") == "(08)" or dictionary.get("Judge Name") == "(09)" or dictionary.get("Judge Name") == "(10)" or dictionary.get("Judge Name") == "(02)" or dictionary.get("Judge Name") == "(East)" or dictionary.get("Judge Name") == "(JUDICIAL DEPARTMENT)" or dictionary.get("Judge Name") == "(Private)" or dictionary.get("Judge Name") == "Justice" or dictionary.get("Judge Name") == "(Guardian Judge)" or dictionary.get("Judge Name") == "(deceased)" or dictionary.get("Judge Name") == "(ii)" or dictionary.get("Judge Name") == "(i)" or dictionary.get("Judge Name") == "(Rev)" or dictionary.get("Judge Name") == "EAST" or dictionary.get("Judge Name") == "(City)" or dictionary.get("Judge Name") == "(MCAC)" or dictionary.get("Judge Name") == "(Private)" or dictionary.get("Judge Name") == "(Legal)" or dictionary.get("Judge Name") == "(Guardian)" : 
            
            
            dictionary["Judge Name"] = random.choice(judges)
    return data


with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\Final Data - judges.json", "r") as file:
    data = json.load(file)
updated_data = fill_empty_fields(data)


with open(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\All Data in JSON\Final Data - judges.json", "w") as file:
    json.dump(updated_data, file, indent=4)
print("Fields updated successfully.")