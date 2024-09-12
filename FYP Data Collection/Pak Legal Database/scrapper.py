from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://www.paklegaldatabase.com/login/')
driver.implicitly_wait(30)

# Initialize empty list to collect all data
all_data = []

# Login handling
# =========================================================
login_form = driver.find_element(By.ID, 'mepr_loginform')
username = login_form.find_element(By.ID, 'user_login')
username.send_keys('methealizain@gmail.com')

password = login_form.find_element(By.ID, 'user_pass')
password.send_keys('A112233@z')

remember_me = login_form.find_element(By.ID, 'rememberme')
remember_me.click()

submit_div = login_form.find_element(By.CSS_SELECTOR, '#mepr_loginform > div.submit')
submit_btn = submit_div.find_element(By.ID, 'wp-submit')
submit_btn.click()
# =========================================================

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

search_button = driver.find_element(By.CLASS_NAME, 'jet-search-filter__input')
search_button.send_keys('family')
search_button.click()


pagination_div = driver.find_element(By.CLASS_NAME, 'jet-filters-pagination')
pagination_item = pagination_div.find_element(By.CLASS_NAME, 'jet-filters-pagination__item')
pagination_links = pagination_item.find_elements(By.CLASS_NAME, 'jet-filters-pagination__link')


# Define the regex pattern for names
names_pattern = r"(.*) VS (.*)"

i = 1

for link in pagination_links:
    link.click() 
    time.sleep(5)

    grid = driver.find_element(By.CLASS_NAME, 'jet-listing-grid__items')
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
            # Extracting names
            h2 = div.find_element(By.CLASS_NAME, 'elementor-heading-title')
            a = h2.find_element(By.TAG_NAME, 'a')
            names = a.text
            match = re.match(names_pattern, names)
            if match:
                data['Client Name'], data['Opponent Name'] = match.groups()
            else:
                print(f'In case {i}, {names} could not be matched.')
        except Exception as e:
            print(f'Error extracting names: {e}')

        try:
            # Extracting Case ID
            case_id_element = div.find_element(By.XPATH, './/div//div//div//div[5]//div')
            data['Case ID'] = case_id_element.text
        except Exception as e:
            print(f'Error extracting Case ID: {e}')

        try:
            # Extracting Court name
            court_name_elements = div.find_elements(By.XPATH, './/div[6]//div//div//div')
            if court_name_elements:
                data['Court'] = court_name_elements[0].text
        except Exception as e:
            print(f'Error extracting Court name: {e}')

        try:
            # Extracting Issue Type
            issue_div = div.find_element(By.XPATH, './/div[7]/div/div')
            issue_spans = issue_div.find_elements(By.TAG_NAME, 'span')
            if issue_spans:
                issue = [span.text for span in issue_spans]
                if issue:
                    data['Issue Type'] = ', '.join(issue)
        except Exception as e:
            print(f'Error extracting Issue Type: {e}')

        try:
            # Extracting Judge Name
            judge_elements = div.find_elements(By.XPATH, './/div[8]/div/div/div')
            if judge_elements:
                data['Judge Name'] = judge_elements[0].text
        except Exception as e:
            print(f'Error extracting Judge Name: {e}')

        try:
            # Extracting Date Filed
            date_element = div.find_element(By.XPATH, './/div[9]/div/div/div')
            data['Date Filed'] = date_element.text
        except Exception as e:
            print(f'Error extracting Date Filed: {e}')

        try:
            # Extracting Case Summary
            case_summary_elements = div.find_elements(By.XPATH, './/div[11]/div/div/div')
            if case_summary_elements:
                data['Summary'] = case_summary_elements[0].text
        except Exception as e:
            print(f'Error extracting Case Summary: {e}')

        all_data.append(data)


        i += 1

# Export data to JSON file
file_path = r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Pak Legal Database"
with open(rf'{file_path}\data_output.json', 'w') as f:
    json.dump(all_data, f, indent=4)

print('Data exported to data_output.json')
print(len(all_data))

driver.quit()
