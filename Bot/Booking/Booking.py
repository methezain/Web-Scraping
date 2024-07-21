from types import TracebackType
from typing import Type
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import Booking.constants as const 
import os

class Booking(webdriver.Firefox):
    def __init__(self, driver_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\Selenium', teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        if self.teardown:
            self.quit() 
        return super().__exit__(exc_type, exc, traceback) 
    
        
    def landing_page(self):
        self.get(const.BASE_URL) 




