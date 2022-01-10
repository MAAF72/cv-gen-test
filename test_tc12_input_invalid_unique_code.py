import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

load_dotenv()

def test_input_invalid_code():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(os.getenv("CHROMEDRIVER"))
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Get page
    browser.get("http://cv-gen-dipl.herokuapp.com:80")

    browser.find_element(By.ID, "input-unique-code").send_keys("W6FK-ZRM5-XXXX")
    browser.find_element(By.ID, "edit-cv").click()
    browser.quit()