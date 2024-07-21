import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\Selenium'

driver = webdriver.Firefox()

driver.get('https://toolsgraphy.blogspot.com/2024/07/text-generator.html') 

driver.implicitly_wait(30)
my_element = driver.find_element(By.ID, 'generate') 
# An alternative way using CSS Selector.
# btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="generateLoremIpsum()"]')
# btn.click() 

copy_element = driver.find_element(By.ID, 'copyButton')  
wordCount = driver.find_element(By.ID, 'wordCount') 
wordCount.send_keys(100) 

my_element.click()  
copy_element.click() 

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.ID, 'copyButton'),
        'Copied'
    ) 
)


