import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')

# Set path to chromedriver as per your configuration
webdriver_service = Service("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Wait for initialize, in seconds
wait = WebDriverWait(browser, 10)

# Get page
browser.get("http://cv-gen-dipl.herokuapp.com:80")

# Extract title from page and print
title = browser.title

# insert unique code
browser.find_element_by_id("input-unique-code").send_keys("W6FK-ZRM5-H20C")
browser.find_element_by_id("edit-cv").click()
time.sleep(5)

# to next page
browser.find_element_by_id("btn-choose-template").click()

# select template
wait.until(EC.presence_of_element_located((By.ID, "template-creative-2")))
browser.find_element_by_id("template-creative-2").click()
time.sleep(1)
browser.find_element_by_id("get-cv").click()

wait.until(EC.alert_is_present())
browser.switch_to.alert.accept()

if browser.find_element_by_xpath('//*[@id="cv-preview-section"]/embed') :
    print('test success')
else:
    print('test failed')

#Wait for 10 seconds
time.sleep(10)
browser.quit()