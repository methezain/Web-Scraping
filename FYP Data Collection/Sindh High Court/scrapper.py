from selenium import webdriver
from selenium.webdriver.common.by import By
from Pdf_Downloader import file_downloader

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://caselaw.shc.gov.pk/caselaw/public/home') 
driver.implicitly_wait(30) 

links = []

blocks = driver.find_elements(By.TAG_NAME, 'blockquote')

for block in blocks:
    if 'FAMILY MATTER' in block.text:
        a = block.find_element(By.TAG_NAME,'a')
        link = a.get_attribute('href')
        links.append(link) 

print(len(links)) 

file_downloader(links) 
    