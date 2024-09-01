import os
import json
from bs4 import BeautifulSoup

file_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Pakistan Legal Research\cases_data'
html_files = [f for f in os.listdir(file_path) if f.endswith('.html')]


case_data = []


for file in html_files:
    file_name = os.path.join(file_path, file)
    with open(file_name, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        case_info = {
            'Case ID': 'nan',
            'Date Filed': 'nan',
            'Client Name': 'nan',
            'Opponent Name': 'nan',
            'Relationship': 'nan',
            'Issue Type': 'nan',
            'Summary': 'nan',
            'Evidence': 'nan',
            'Witnesses': 'nan',
            'Legal Precedents': 'nan',
            'Court': 'nan',
            'Judge Name': 'nan',
            'Outcome': 'nan',
            'Appeal': 'nan'
        }
        
        
    case_id = ''
    h4_tags = soup.find_all('h4')
    for h4_tag in h4_tags:
        strong_tag = h4_tag.find('strong')
        if strong_tag:
            u_tag = strong_tag.find('u')
            if u_tag and u_tag.string == 'Case Citation:':
                p_tag = h4_tag.find_next_sibling('p')
                if p_tag:
                    case_id = p_tag.get_text()
                    case_info['Case ID'] = case_id
        
        
        
    date_filed_tag = soup.find('h4', string='Date Filed:')
    if date_filed_tag:
        case_info['Date Filed'] = date_filed_tag.text.strip() 
        
        
    client_name_tag = soup.find('h4', string='Parties:')
    if client_name_tag:
        ul_tag = client_name_tag.find_next_sibling('ul')
        if ul_tag:
            li_tags = ul_tag.find_all('li')
            if len(li_tags) > 1:  
                case_info['Client Name'] = li_tags[0].text.strip() 
    
    
    opponent_name_tag = soup.find('h4', string='Parties:')
    if opponent_name_tag:
        ul_tag = opponent_name_tag.find_next_sibling('ul')
        if ul_tag:
            li_tags = ul_tag.find_all('li')
            if len(li_tags) > 1:  
                case_info['Opponent Name'] = li_tags[1].text.strip()

        
    relationship_tag = soup.find('h4', string='Relationship:')
    if relationship_tag:
        case_info['Relationship'] = relationship_tag.find_next_sibling('p').text.strip()
        
        
    issue_type_tag = soup.find('h4', string='Issues:')
    if issue_type_tag:
        case_info['Issue Type'] = issue_type_tag.find_next_sibling('p').text.strip()
        
    summary_tag = soup.find('h4', string='Issues Addressed:')
    if summary_tag:
        case_info['Summary'] = summary_tag.find_next_sibling('p').text.strip()
        
    evidence_tag = soup.find('h4', string='Evidence:')
    if evidence_tag:
        evidence_list = []
        for item in evidence_tag.find_next_sibling('ul').find_all('li'):
            evidence_list.append(item.text.strip())
        case_info['Evidence'] = evidence_list
        
    witnesses_tag = soup.find('h4', string='Witnesses:')
    if witnesses_tag:
        witnesses_list = []
        for item in witnesses_tag.find_next_sibling('ul').find_all('li'):
            witnesses_list.append(item.text.strip())
        case_info['Witnesses'] = witnesses_list
            
    legal_precedents_tag = soup.find('h4', string='Legal Precedents:')
    if legal_precedents_tag:
        legal_precedents_list = []
        for item in legal_precedents_tag.find_next_sibling('ul').find_all('li'):
            legal_precedents_list.append(item.text.strip())
        case_info['Legal Precedents'] = legal_precedents_list
        
        
    court_tag = soup.find('h4', string='Court:')
    if court_tag:
        case_info['Court'] = court_tag.find_next_sibling('p').text.strip()
        
        
        
    judges_name_list = []
    
    h4_tags = soup.find_all('h4')
    for h4_tag in h4_tags:
        strong_tag = h4_tag.find('strong')
        if strong_tag:
            u_tag = strong_tag.find('u')
            if u_tag and u_tag.string == 'Judges' or u_tag.string == 'Judges:':
                ul_tag = h4_tag.find_next_sibling('ul')
                if ul_tag:
                    for item in ul_tag.find_all('li'):
                        judges_name_list.append(item.text.strip())
                break 

    case_info['Judge Name'] = judges_name_list
    
    outcome_tag = soup.find('h4', string='Court Held:')
    if outcome_tag:
        case_info['Outcome'] = outcome_tag.find_next_sibling('p').text.strip() 



    case_data.append(case_info)

    output_file = 'case_data.json'
    with open(os.path.join(file_path, output_file), 'w', encoding='utf-8') as json_file:
        json.dump(case_data, json_file, ensure_ascii=False, indent=4)

    
    