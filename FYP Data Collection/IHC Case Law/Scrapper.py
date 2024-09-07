from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from downloader import file_downloader


driver = webdriver.Firefox()
driver.maximize_window()

landing_page = driver.get('https://mis.ihc.gov.pk/frmSrchOrdr')
driver.implicitly_wait(30)
search_field = driver.find_element(By.ID, 'txtKyWrd')
search_field.click()
search_field.send_keys('Family')
search_button = driver.find_element(By.ID, 'btnSearch')
search_button.click()
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)
main_div = driver.find_elements(By.CSS_SELECTOR, '#dvMain > div') 
links_list = []

for div in main_div: 
    buttons_div = div.find_element(By.ID,'dwnld') 
    a_button = buttons_div.find_element(By.XPATH,'.//a/center/i')
    a_button.click() 
    
    driver.switch_to.window(driver.window_handles[-1])
    
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    
    dwnd_row = driver.find_element(By.XPATH, "/html/body/div[2]/section/div[1]")
    dwnd_btn = dwnd_row.find_element(By.XPATH,'/html/body/div[2]/section/div[1]/div[4]/a')
    link = dwnd_btn.get_attribute('href')
    
    links_list.append(link) 
    driver.close()
    
    driver.switch_to.window(driver.window_handles[0]) 
    
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )



for i,link in enumerate(links_list, start=1):
    print(link) 


file_downloader(links_list) 
