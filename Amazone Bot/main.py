from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

driver = webdriver.Firefox()
driver.maximize_window() 

query = 'laptop'
file_no = 1

for i in range(1,20):  
    landing_page = driver.get(f'https://www.amazon.com/s?k={query}&page={i}&crid=44KEHOSV90UW&sprefix=lapto%2Caps%2C419&ref=nb_sb_noss_2') 

    driver.implicitly_wait(10)

    laptop_cards = driver.find_elements(By.CLASS_NAME , 'puis-card-container')

    print(f"{len(laptop_cards)} items found.\n\n")
    
    for card in laptop_cards:
            try:
                data = card.get_attribute('outerHTML')
                with open(f'{query}_{file_no}.html', 'w', encoding='utf-8') as f:
                    f.write(data) 
                    file_no += 1 
            except Exception as e:
                print(f"Error writing file {query}_{i}_{file_no}.html: {e}")


driver.close()
print("exiting ...") 
 












