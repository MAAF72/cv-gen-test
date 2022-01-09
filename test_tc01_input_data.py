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

def test_tc01_input_data():
    PHOTO_PATH = os.path.join(os.getcwd(), 'resources', 'photo.png')

    ## Setup chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(os.getenv("CHROME_DRIVER_PATH"))

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

    with pytest.raises(Exception, match="no such alert"):
        browser.switch_to.alert

    fill('#form-customer #nama', 'John Doe')
    fill('#form-customer #email', 'john.doe@github.com')
    fill('#form-customer #no_hp', '085335831111')
    fill('#form-customer #portfolio', 'john-doe.github.io')
    fill('#form-customer #job', 'Quality Assurance')
    fill('#form-customer #deskripsi', 'Tester')

    click('#form-socialmedia .content-socialmedia:last-child #delete-socialmedia')

    click('#form-edukasi .content-edukasi:last-child #delete-edukasi')

    click('#form-penghargaan .content-penghargaan:last-child #delete-penghargaan')

    click('#form-pengalaman .content-pengalaman:last-child #delete-pengalaman')

    click('#form-rujukan .content-rujukan:last-child #delete-rujukan')

    click('#form-bahasa .content-bahasa:last-child #delete-bahasa')

    click('#form-kemampuan .content-kemampuan:last-child #delete-kemampuan')

    browser.execute_script("window.scroll(0, 0);")

    click('#btn-choose-template')

    WebDriverWait(browser, 10).until(EC.title_is('Choose Template'))

    assert browser.title == "Choose Template"

    browser.quit()