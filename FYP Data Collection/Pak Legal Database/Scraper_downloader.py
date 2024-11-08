from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json
import time
from selenium.webdriver.common.keys import Keys


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
username.send_keys('hammadgul998@gmail.com')

password = login_form.find_element(By.ID, 'user_pass')
password.send_keys('Hammad.@123')

remember_me = login_form.find_element(By.ID, 'rememberme')
remember_me.click()

submit_div = login_form.find_element(By.CSS_SELECTOR, '#mepr_loginform > div.submit')
submit_btn = submit_div.find_element(By.ID, 'wp-submit')
submit_btn.click()
# =========================================================

time.sleep(3) 

search_button = driver.find_element(By.CLASS_NAME, 'jet-search-filter__input')
search_button.send_keys('family')
search_button.send_keys(Keys.ENTER)

time.sleep(5) 



pagination_div = driver.find_element(By.CLASS_NAME, 'jet-filters-pagination') 
pagination_item = pagination_div.find_element(By.CLASS_NAME, 'jet-filters-pagination__item')
# pagination_links = pagination_item.find_elements(By.CLASS_NAME, 'jet-filters-pagination__link')
i = 1

# Define the regex pattern for names
names_pattern = r"(.*)\s*(?:VS|Vs|V\.|vs|v\.|V/S|VERSUS|versus|Versus)\s*(.*)"


def scroll_into_view(element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(3) 
    
pagi_element = driver.find_element(By.XPATH,'/html/body/div[1]/div/section[1]/div/div[2]/div/div/div/div/section[2]/div/div/div/div[2]')
pagi_container = pagi_element.find_element(By.CLASS_NAME,'elementor-widget-container')
pagi_subdiv = pagi_container.find_element(By.XPATH,'/html/body/div[1]/div/section[1]/div/div[2]/div/    div/div/div/section[2]/div/div/div/div[2]/div/div')
pagination = pagi_subdiv.find_element(By.CLASS_NAME,'jet-filters-pagination')
page_items = pagination.find_elements(By.CLASS_NAME, 'jet-filters-pagination__item') 
print(len(page_items))
print(len(page_items)) 

pdf_links = []

import requests
while True:
    
    grid = driver.find_element(By.CLASS_NAME, 'jet-listing-grid__items')
    divs = grid.find_elements(By.CLASS_NAME, 'jet-listing-grid__item')
    
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'jet-listing-grid__item'))
    )


    for div in divs:
        view_pdf = div.find_element(By.XPATH, ".//a[text()='Download PDF']") 
        pdf = view_pdf.get_attribute("href") 
        response = requests.get(pdf)
        if response.status_code == 200:
            with open(rf"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Pak Legal Database\pdf's\file_{i}.pdf", "wb") as file:
                file.write(response.content)
            print(f"Downloaded file_{i}.pdf")
            i += 1
        else:
            print(f"Failed to download from {pdf}") 
        
        


    print(len(pdf_links))
    
    pagi_element = driver.find_element(By.XPATH,'/html/body/div[1]/div/section[1]/div/div[2]/div/div/div/div/section[2]/div/div/div/div[2]')
    pagi_container = pagi_element.find_element(By.CLASS_NAME,'elementor-widget-container')
    pagi_subdiv = pagi_container.find_element(By.XPATH,'/html/body/div[1]/div/section[1]/div/div[2]/div/    div/div/div/section[2]/div/div/div/div[2]/div/div')
    pagination = pagi_subdiv.find_element(By.CLASS_NAME,'jet-filters-pagination')
    page_items = pagination.find_elements(By.CLASS_NAME, 'jet-filters-pagination__item')
    
    driver.execute_script("arguments[0].style.display='none';", pagi_element)
    next_btn = pagination.find_element(By.CSS_SELECTOR,'div[data-value="next"]') 
    driver.execute_script("arguments[0].style.display='block';", next_btn)
    
    if next_btn.get_attribute('disabled') is None:
        driver.execute_script("arguments[0].click();", next_btn)
        WebDriverWait(driver, 15).until(
            EC.staleness_of(grid)
        )
        time.sleep(5) 
    else:
        print("Next button is disabled Now.")
        break
    
