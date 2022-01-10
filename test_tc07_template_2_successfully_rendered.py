import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

load_dotenv()

def test_template_2_successfuly_rendered():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(os.getenv("CHROMEDRIVER"))
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Wait for initialize, in seconds
    wait = WebDriverWait(browser, 10)

    # Get page
    browser.get("http://cv-gen-dipl.herokuapp.com:80")

    # insert unique code
    browser.find_element(By.ID, "input-unique-code").send_keys("W6FK-ZRM5-H20C")
    browser.find_element(By.ID, "edit-cv").click()
    time.sleep(5)

    # to next page
    browser.find_element(By.ID, "btn-choose-template").click()

    # select template
    wait.until(EC.presence_of_element_located((By.ID, "template-creative-2")))
    browser.find_element(By.ID, "template-creative-2").click()
    time.sleep(1)
    browser.find_element(By.ID, "get-cv").click()

    wait.until(EC.alert_is_present())
    browser.switch_to.alert.accept()

    assert browser.find_element(By.XPATH, '//*[@id="cv-preview-section"]/embed'), 'CV template is not rendered'
    browser.quit()