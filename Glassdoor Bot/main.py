from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Firefox()

driver.get('https://www.glassdoor.com/index.htm')
driver.implicitly_wait(10) 

login_options = driver.find_element(By.XPATH, '/html/body/div[3]/section[1]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/button')





# search = driver.find_element(By.ID, 'searchBar-jobTitle')
# search.send_keys('Python') 

# location = driver.find_element(By.ID, 'searchBar-location')
# search.send_keys('United States') 
