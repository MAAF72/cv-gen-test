import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def browser_fill(browser, selector, value):
    obj = browser.find_element(By.CSS_SELECTOR, selector)
    obj.send_keys(value)

    return obj

def browser_click(browser, selector):
    obj = browser.find_element(By.CSS_SELECTOR, selector)
    obj.click()

    return obj

def browser_select(browser, selector, value):
    obj = browser.find_element(By.CSS_SELECTOR, selector)
    select = Select(obj)
    select.select_by_visible_text(value)

    return obj

def test_tc03_invalid_image_size():
    PHOTO_PATH = f'{os.getcwd()}/resources/Fatih.png'

    ## Setup chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Set path to chromedriver as per your configuration
    webdriver_service = Service("/snap/bin/chromium.chromedriver")

    # Choose Chrome Browser
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Define some helper to make easier
    fill = lambda selector, val: browser_fill(browser, selector, val)
    click = lambda selector: browser_click(browser, selector)
    select = lambda selector, val: browser_select(browser, selector, val)

    # Get page
    browser.get("http://cv-gen-dipl.herokuapp.com:80")

    assert browser.title == "Landing page", "wrong landing page"

    click('#create-cv')

    assert browser.title == "Input Data", "wrong input data page"

    fill('#form-customer #photo', PHOTO_PATH)

    assert browser.switch_to.alert.text == "invalid image size", "invalid image size passed"

    browser.quit()