from types import TracebackType
from selenium.webdriver.common.by import By
from selenium import webdriver
from constants import BASE_URL
import os

# driver_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\Selenium'
# driver = webdriver.Firefox() 

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# browser = webdriver.Chrome(executable_path=r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\Selenium')



class Booking(webdriver.Firefox): 
    
    def __init__(self, driver_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\Selenium'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super().__init__()
        self.maximize_window()
            
    # def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
    #     self.quit()
        
    def landing_page(self):
        self.get(BASE_URL) 
        
    def discover(self):
        button = self.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[1]/a/span') 
        button.click()
        
    def dismiss_signin(self):
        cross_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
        cross_depth = cross_button.svg
        self.implicitly_wait(10)
        cross_depth.click()

    def select_currency(self):
        current_Currency = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Prices in Pakistani Rupee"]/span')
        current_Currency.click()


