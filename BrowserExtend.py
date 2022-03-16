import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BrowserExtend(webdriver.Chrome):
    def __init__(self):
        ## Setup chrome options
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        # Set path to chromedriver as per your configuration
        webdriver_service = Service(os.getenv("CHROME_DRIVER_PATH"))

        super(BrowserExtend, self).__init__(service=webdriver_service, options=chrome_options)
        
    def fill(self, selector, value):
        obj = self.find_element(By.CSS_SELECTOR, selector)
        obj.send_keys(value)

        return obj

    def click(self, selector):
        obj = self.find_element(By.CSS_SELECTOR, selector)
        obj.click()

        return obj

    def select(self, selector, value):
        obj = self.find_element(By.CSS_SELECTOR, selector)
        select = Select(obj)
        select.select_by_visible_text(value)

        return obj

    def wait_title(self, title):
        WebDriverWait(self, 10).until(EC.title_is(title))