from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

landing_page = driver.get('https://pakistanlegalresearch.com/')
driver.implicitly_wait(30)

search_button = driver.find_element(By.CLASS_NAME, 'fa-magnifying-glass')
search_button.click()

search_input = driver.find_element(By.CLASS_NAME, 'search-input')
query = search_input.send_keys('family law')
hit_enter = search_input.send_keys(Keys.ENTER)
driver.implicitly_wait(15)

enter_family_cases = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[1]/div[3]/div[1]/ol/li[1]/h3/a')
enter_family_cases.click()

figure = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/article/div/div[2]/div[1]/figure[1]')
table = figure.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/article/div/div[2]/div[1]/figure[1]/table')

table_rows = table.find_elements(By.TAG_NAME, 'tr') 
cases_links = [] 

for row in table_rows:
    try:
        td = row.find_element(By.TAG_NAME, 'td')
        a = td.find_element(By.TAG_NAME, 'a')
        cases_links.append(a.get_attribute('href')) 
    except Exception:
        continue

file_no = 1
files_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\cases_data'

for link in cases_links:
    try:
        driver.get(link) 
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        case_data = driver.page_source
        with open(rf'{files_path}\case_{file_no}.html', 'w', encoding='utf-8') as f:
            f.write(case_data)
        file_no += 1
    except Exception as e:
        print(e)
    time.sleep(1) 

driver.quit()