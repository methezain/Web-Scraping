from selenium import webdriver
from selenium.webdriver.common.by import By
import time

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--disable-notifications")

driver = webdriver.Firefox(options=firefox_options)

driver.get('https://www.glassdoor.com/Job/index.htm')

time.sleep(5)

try:
    close_button = driver.find_element(By.ID, 'Close')
    close_button.click()
except Exception as e:
    print("Pop-up close button not found or unable to close the pop-up.", e)

