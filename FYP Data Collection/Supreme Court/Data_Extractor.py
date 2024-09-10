import os
import re
import json

court_name_pattern = r"ORDER SHEET\b\s*\n(?:\s*\n)*(.+?)(?:\n|$)"
date_pattern = r"\d{2}[-.]\d{2}[-.]\d{4}"
client_opponent_pattern = r"(.*)\s+VS\s+(.*)"
case_id_pattern = r'NO\.\s*([^\n]*)'
judge_name_pattern = r"MR\. JUSTICE [A-Z\s.-]{2,}"
summary_pattern = r"(?<=ORDER SUMMARY:)([\s\S]*)"

def extract_data_from_file(file_path: str) -> tuple:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read() 

        court_name_match = re.search(court_name_pattern, text, re.DOTALL | re.IGNORECASE)
        court_name = court_name_match.group(1).strip() if court_name_match else "Court name not found"

        client_name, opponent_name = "Client name not found", "Opponent name not found"

        case_start_index = text.find(court_name) + len(court_name)
        case_text = text[case_start_index:]

        date_match = re.search(date_pattern, text, re.DOTALL | re.IGNORECASE)
        date = date_match.group(0).strip() if date_match else "Date not found"

        case_id_match = re.search(case_id_pattern, text, re.DOTALL | re.IGNORECASE)
        case_id = case_id_match.group(1).strip() if case_id_match else "Case ID not found"

        judge_name_match = re.search(judge_name_pattern, text, re.DOTALL | re.IGNORECASE)
        judge_name = judge_name_match.group(0).strip() if judge_name_match else "Judge name not found"

        client_opponent_match = re.search(client_opponent_pattern, text, re.DOTALL)
        if client_opponent_match:
            client_name = client_opponent_match.group(1).strip()
            opponent_name = client_opponent_match.group(2).strip()

        date_index = text.find(date)
        judge_name_index = text.find(judge_name)

        if date_index != -1 and judge_name_index != -1:
            summary_text = text[date_index + len(date):judge_name_index].strip()
        else:
            summary_text = "Summary not found"

        extracted_data = {
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

        missing_values = {key: value for key, value in extracted_data.items() if value.endswith("not found") or value.strip() == ""}

        output_dir = r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Supreme Court\Cases_JSON"
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, "output.json")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(extracted_data, f, indent=4)

        return extracted_data, missing_values

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}, {}

file_path = r"E:\input file\output.txt"  # Make sure this is a valid path

extract_data_from_file(file_path)
