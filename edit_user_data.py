import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')

# Set path to chromedriver as per your configuration
webdriver_service = Service("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Get page
browser.get("http://cv-gen-dipl.herokuapp.com:80")

# Extract title from page and print
title = browser.title

# insert unique code
browser.find_element_by_id("input-unique-code").send_keys("W6FK-ZRM5-H20C")
browser.find_element_by_id("edit-cv").click()
time.sleep(3)

# edit data
browser.find_element_by_id("nama").clear()
browser.find_element_by_id("nama").send_keys("John Doe 2")
browser.find_element_by_id("email").clear()
browser.find_element_by_id("email").send_keys("johndoe2@gmail.com")
browser.find_element_by_id("no_hp").clear()
browser.find_element_by_id("no_hp").send_keys("085335831122")
browser.find_element_by_id("portfolio").clear()
browser.find_element_by_id("portfolio").send_keys("maaf72@github.io")
browser.find_element_by_id("job").clear()
browser.find_element_by_id("job").send_keys("Quality Assurance")
browser.find_element_by_id("deskripsi").clear()
browser.find_element_by_id("deskripsi").send_keys("Tester")
browser.find_element_by_id("btn-choose-template").click()

#Wait for 10 seconds
time.sleep(10)
browser.quit()