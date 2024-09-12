from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json
import os

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://www.paklegaldatabase.com/login/')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'mepr_loginform')))

login_form = driver.find_element(By.ID, 'mepr_loginform')
username = login_form.find_element(By.ID, 'user_login')
username.send_keys('methealizain@gmail.com')

password = login_form.find_element(By.ID, 'user_pass')
password.send_keys('A112233@z')

remember_me = login_form.find_element(By.ID, 'rememberme')
remember_me.click()

submit_btn = login_form.find_element(By.ID, 'wp-submit')
submit_btn.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

search_button = driver.find_element(By.CLASS_NAME, 'jet-search-filter__input')
search_button.send_keys("Family")
search_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'jet-listing-grid__items')))

all_data = []

names_pattern = r"(.*) VS (.*)"
file_path = r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Pak Legal Database"

if not os.path.exists(file_path):
    os.makedirs(file_path)

i = 1
while True:
    grid = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'jet-listing-grid__items'))
    )
    divs = grid.find_elements(By.CLASS_NAME, 'jet-listing-grid__item')

    for div in divs:
        data = {
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

        try:
            h2 = WebDriverWait(div, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'elementor-heading-title'))
            )
            a = h2.find_element(By.TAG_NAME, 'a')
            names = a.text
            match = re.match(names_pattern, names)
            if match:
                data['Client Name'], data['Opponent Name'] = match.groups()
        except Exception as e:
            print(f'Error extracting names: {e}')

        try:
            case_id_element = WebDriverWait(div, 10).until(
                EC.presence_of_element_located((By.XPATH, './/div//div//div//div[5]//div'))
            )
            data['Case ID'] = case_id_element.text
        except Exception as e:
            print(f'Error extracting Case ID: {e}')

        try:
            court_name_element = WebDriverWait(div, 10).until(
                EC.presence_of_element_located((By.XPATH, './/div[6]//div//div//div'))
            )
            data['Court'] = court_name_element.text
        except Exception as e:
            print(f'Error extracting Court name: {e}')

        try:
            issue_div = WebDriverWait(div, 10).until(
                EC.presence_of_element_located((By.XPATH, './/div[7]/div/div'))
            )
            issue_spans = issue_div.find_elements(By.TAG_NAME, 'span')
            issue = [span.text for span in issue_spans]
            data['Issue Type'] = ', '.join(issue) if issue else 'nan'
        except Exception as e:
            print(f'Error extracting Issue Type: {e}')

        try:
            judge_element = WebDriverWait(div, 10).until(
                EC.presence_of_element_located((By.XPATH, './/div[8]/div/div/div'))
            )
            data['Judge Name'] = judge_element.text
        except Exception as e:
            print(f'Error extracting Judge Name: {e}')

        try:
            date_element = WebDriverWait(div, 10).until(
                EC.presence_of_element_located((By.XPATH, './/div[9]/div/div/div'))
            )
            data['Date Filed'] = date_element.text
        except Exception as e:
            print(f'Error extracting Date Filed: {e}')

        try:
            case_summary_element = WebDriverWait(div, 10).until(
                EC.presence_of_element_located((By.XPATH, './/div[11]/div/div/div'))
            )
            data['Summary'] = case_summary_element.text
        except Exception as e:
            print(f'Error extracting Case Summary: {e}')

        all_data.append(data)
        i += 1

    try:
        next_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'next'))
        )
        next_btn.click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'jet-listing-grid__items')))
    except Exception as e:
        print(f"No more pages or error clicking next: {e}")
        break

with open(rf'{file_path}\data_output.json', 'w') as f:
    json.dump(all_data, f, indent=4)

print('Data exported to data_output.json')
print(len(all_data))

driver.quit()
