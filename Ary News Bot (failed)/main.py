from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def scrap_ARY():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://arynews.tv/category/sci-techno/') 
    driver.implicitly_wait(10)
    data = {'Post Title':[], 'Post Link':[]}
    
    pages_to_scrap = 0
    
    while pages_to_scrap <= 20:
        entries = driver.find_elements(By.CLASS_NAME, 'entry-title') 
        for entry in entries:
            t = entry.find_element(By.TAG_NAME, 'a') 
            title = t.text
            link = t.get_attribute('href') 

            data['Post Title'].append(title) 
            data['Post Link'].append(link) 
        
        try:
            #remove ad that is hiding the load more button
            driver.execute_script("""
                var elements = document.getElementsByClassName('catfish-ad-container');
                for (var i = 0; i < elements.length; i++) {
                elements[i].style.display = 'none';
                }
            """)

            
            button = driver.find_element(By.CLASS_NAME, 'td-load-more-wrap')
            load_more = button.find_element(By.ID, 'next-page-tdi_60')
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            
            load_more.click() 
            time.sleep(3) 
            
        except Exception as e:
            print("No Load More button is found.", e)
            break 
        
        pages_to_scrap += 1
        
    return data


def export_csv():
    df = scrap_ARY() 
    export_data = pd.DataFrame(df) 
    export_data.to_csv('Ary_News_tech_section.csv', index=False) 


#main 
export_csv() 

