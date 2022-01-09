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
    PHOTO_PATH = f'{os.getcwd()}/resources/photo.png'

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

    with pytest.raises(Exception, match="no such alert"):
        browser.switch_to.alert

    fill('#form-customer #nama', 'John Doe')
    fill('#form-customer #email', 'john.doe@github.com')
    fill('#form-customer #no_hp', '085335831111')
    fill('#form-customer #portfolio', 'john-doe.github.io')
    fill('#form-customer #job', 'Quality Assurance')
    fill('#form-customer #deskripsi', 'Tester')

    fill('#form-socialmedia .content-socialmedia:last-child #nama', 'Facebook')
    fill('#form-socialmedia .content-socialmedia:last-child #link', 'fb.com/john.doe')
    click('#add-socialmedia')
    fill('#form-socialmedia .content-socialmedia:last-child #nama', 'Instagram')
    fill('#form-socialmedia .content-socialmedia:last-child #link', 'ig.com/john.doe')

    fill('#form-edukasi .content-edukasi:last-child #jenjang', 'S1')
    fill('#form-edukasi .content-edukasi:last-child #instansi', 'Telkom University')
    fill('#form-edukasi .content-edukasi:last-child #tahun_mulai', '09/03/2018')
    fill('#form-edukasi .content-edukasi:last-child #tahun_selesai', '01/01/2022')
    fill('#form-edukasi .content-edukasi:last-child #deskripsi', 'S1 Informatika with 3.99 GPA')

    fill('#form-penghargaan .content-penghargaan:last-child #nama', 'Best Apps')
    fill('#form-penghargaan .content-penghargaan:last-child #instansi', 'Arkavidia 5.0')
    fill('#form-penghargaan .content-penghargaan:last-child #tahun', '01/01/2019')
    fill('#form-penghargaan .content-penghargaan:last-child #deskripsi', 'CV Generator get Best Apps award at annualy informatics competition Arkavidia 5.0, held by Institut Teknologi Bandung')

    fill('#form-pengalaman .content-pengalaman:last-child #nama', 'Junior Software Engineer')
    fill('#form-pengalaman .content-pengalaman:last-child #instansi', 'PT Proclub Studio Indonesia')
    fill('#form-pengalaman .content-pengalaman:last-child #tahun_mulai', '01/04/2021')
    fill('#form-pengalaman .content-pengalaman:last-child #tahun_selesai', '01/09/2021')
    fill('#form-pengalaman .content-pengalaman:last-child #deskripsi', 'Do backend stuff with golang and some dev-op things')

    fill('#form-rujukan .content-rujukan:last-child #nama', 'Doe Jhon')
    fill('#form-rujukan .content-rujukan:last-child #instansi', 'PT Haha Hihi Project')
    fill('#form-rujukan .content-rujukan:last-child #no_hp', '081291734621')
    fill('#form-rujukan .content-rujukan:last-child #email', 'doe.jhon@hahahihi.com')

    fill('#form-bahasa .content-bahasa:last-child #nama', 'Indonesia')
    select('#form-bahasa .content-bahasa:last-child #level', 'Native')
    click('#add-bahasa')
    fill('#form-bahasa .content-bahasa:last-child #nama', 'English')
    select('#form-bahasa .content-bahasa:last-child #level', 'Professional')
    click('#add-bahasa')
    fill('#form-bahasa .content-bahasa:last-child #nama', 'Java')
    select('#form-bahasa .content-bahasa:last-child #level', 'Elementary')

    fill('#form-kemampuan .content-kemampuan:last-child #nama', 'Programming')
    click('#add-kemampuan')
    fill('#form-kemampuan .content-kemampuan:last-child #nama', 'Problem Solving')
    click('#add-kemampuan')
    fill('#form-kemampuan .content-kemampuan:last-child #nama', 'Web Designing')
    click('#add-kemampuan')
    fill('#form-kemampuan .content-kemampuan:last-child #nama', 'Researching')


    browser.execute_script("window.scroll(0, 0);")

    click('#btn-choose-template')

    WebDriverWait(browser, 10).until(EC.title_is('Choose Template'))

    assert browser.title == "Choose Template"

    browser.quit()