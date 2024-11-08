import os
import re
import json
from re import MULTILINE

court_name_pattern = r"ORDER SHEET\s*\n(?:\s*\n)*(.+?)(?:\n|$)"
date_pattern = r"\d{2}[-.]\d{2}[-.]\d{4}"
case_id_pattern = r"No\.\s*([^\n]+)"
summary_pattern = r"-{3,}\s*(?:\r?\n\s*)+(.+)" 



def extract_data_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()

    court_name_match = re.search(court_name_pattern, text, re.DOTALL | re.IGNORECASE)
    court_name = court_name_match.group(1).strip() if court_name_match else "Court name not found"

    date_match = re.search(date_pattern, text, re.DOTALL | re.IGNORECASE)
    date = date_match.group(0).strip() if date_match else "Date not found"

    case_id_match = re.search(case_id_pattern, text, re.DOTALL | re.IGNORECASE)
    case_id = case_id_match.group(0).strip() if case_id_match else "case id not found"

    date_index = text.find(date_pattern)

    summary_text_match = re.search(summary_pattern, text, re.DOTALL | re.IGNORECASE) 
    summary_text = summary_text_match.group(1).strip() if summary_text_match else "Summary not found"
    
    data = {
        "Case Id": case_id,
        "Date Filed": date,
        "Client Name": "nan",
        "Opponent Name": "nna",
        "Relationship": 'nan',
        "Issue Type": 'nan',
        "Summary": summary_text,
        "Evidence": 'nan',
        "Witnesses":'nan',
        "Legal Precedents": "nan",
        "Court": 'High Court of Sindh, Karachi',
        "Judge Name": "nan",
        "Outcome": 'nan',
        "Appeal": 'nan'
    }

    missing_values = {key: value for key, value in data.items() if value.endswith("not found") or value.strip() == ""}

    return data, missing_values


directory_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Sindh High Court\Cases Txt' 

all_data = []

for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        txt_file = os.path.join(directory_path, filename)
        data, missing_values = extract_data_from_txt(txt_file)
        all_data.append(data)  

file_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Sindh High Court\Cases JSON'
with open(rf'{file_path}\output.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=4)