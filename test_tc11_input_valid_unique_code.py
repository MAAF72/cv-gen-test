import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_input_valid_code():
    ## Setup chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')

    # Set path to chromedriver as per your configuration
    webdriver_service = Service("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")

    # Choose Chrome Browser
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Get page
    browser.get("http://cv-gen-dipl.herokuapp.com:80")

    browser.find_element(By.ID, "input-unique-code").send_keys("W6FK-ZRM5-H20C")
    browser.find_element(By.ID, "edit-cv").click()

    assert browser.title == 'Edit Data'
    browser.quit()