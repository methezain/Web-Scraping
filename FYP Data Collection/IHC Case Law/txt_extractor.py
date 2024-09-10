import os
import re
import json
from re import MULTILINE

court_name_pattern = r"ORDER SHEET\s*\n(?:\s*\n)*(.+?)(?:\n|$)"
date_pattern = r"\d{2}[-.]\d{2}[-.]\d{4}"
client_opponent_pattern = r"(.*)\s+VS\s+(.*)"
case_id_pattern = r'NO\.\s*([^\n]*)'
judge_name_pattern = r"\((.*?)\)"
summary_pattern = r'([^\n]*)'


def extract_data_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()

    court_name_match = re.search(court_name_pattern, text, re.DOTALL | re.IGNORECASE)
    court_name = court_name_match.group(1).strip() if court_name_match else "Court name not found"

    client_name, opponent_name = "Client name not found", "Opponent name not found"
    
    case_start_index = text.find(court_name) + len(court_name)
    case_text = text[case_start_index:]

    date_match = re.search(date_pattern, text, re.DOTALL | re.IGNORECASE)
    date = date_match.group(0).strip() if date_match else "Date not found"

    case_id_match = re.search(case_id_pattern, text, re.DOTALL | re.IGNORECASE)
    case_id = case_id_match.group(0).strip() if case_id_match else "case id not found"
    
    judge_name_match = re.search(judge_name_pattern, text, re.DOTALL | re.IGNORECASE)
    judge_name = judge_name_match.group(0).strip() if judge_name_match else "judge name not found"

    client_opponent_match = re.search(client_opponent_pattern, text, re.MULTILINE)  
    if client_opponent_match:
        client_name = client_opponent_match.group(1).strip()
        opponent_name = client_opponent_match.group(2).strip()

    date_index = text.find(date)
    judge_name_index = text.find(judge_name)

    summary_text = text[date_index + len(date):judge_name_index]
    summary_text = summary_text.strip()

    # Create a dictionary to store the extracted data
    data = {
        "Case Id": case_id,
        "Date Filed": date,
        "Client Name": client_name,
        "Opponent Name": opponent_name,
        "Relationship": 'nan',
        "Issue Type": 'nan',
        "Summary": summary_text,
        "Evidence": 'nan',
        "Witnesses":'nan',
        "Legal Precedents": "nan",
        "Court": 'Islamabad High Court.',
        "Judge Name": judge_name,
        "Outcome": 'nan',
        "Appeal": 'nan'
    }

    # Check for missing values
    missing_values = {key: value for key, value in data.items() if value.endswith("not found") or value.strip() == ""}

    return data, missing_values

# Specify the directory path
directory_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\IHC Case Law\Output TXT'
all_data = []

# Iterate over the files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        txt_file = os.path.join(directory_path, filename)
        data, missing_values = extract_data_from_txt(txt_file)
        all_data.append(data)  # Append the extracted data to the list

# Create a JSON file to store the extracted data
file_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\IHC Case Law\Cases JSON'
with open(rf'{file_path}\output.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=4)