import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

load_dotenv()

def test_edit_user_data():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(os.getenv("CHROMEDRIVER"))
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Get page
    browser.get("http://cv-gen-dipl.herokuapp.com:80")

    # insert unique code
    browser.find_element(By.ID, "input-unique-code").send_keys("W6FK-ZRM5-H20C")
    browser.find_element(By.ID, "edit-cv").click()
    time.sleep(3)

    # edit data
    browser.find_element(By.ID, "nama").clear()
    browser.find_element(By.ID, "nama").send_keys("John Doe 2")
    browser.find_element(By.ID, "email").clear()
    browser.find_element(By.ID, "email").send_keys("johndoe2@gmail.com")
    browser.find_element(By.ID, "no_hp").clear()
    browser.find_element(By.ID, "no_hp").send_keys("085335831122")
    browser.find_element(By.ID, "portfolio").clear()
    browser.find_element(By.ID, "portfolio").send_keys("maaf72@github.io")
    browser.find_element(By.ID, "job").clear()
    browser.find_element(By.ID, "job").send_keys("Quality Assurance")
    browser.find_element(By.ID, "deskripsi").clear()
    browser.find_element(By.ID, "deskripsi").send_keys("Tester")
    browser.find_element(By.ID, "btn-choose-template").click()

    time.sleep(5)
    assert browser.title == 'Choose Template'
    browser.quit()