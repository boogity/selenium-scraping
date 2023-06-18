### Basic Selenium tutorial following the official docs to better understand Se
# https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Initialize the driver that will interface with our browser (requires a valid browser installed and in $PATH)
driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
# Validate that title for this page is what we expect it to be 
assert title == "Web form"

# Why do we wait? Wasn't explained well in the selenium tutorial. Elements to load in? Become interactive?
driver.implicitly_wait(0.5)

# Finding elements
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# Taking actions on elements
text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
value = message.text
assert value == "Received!"

# Close the browser
driver.quit()