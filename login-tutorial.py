### Tutorial code for testing logins with github.com
# https://www.thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python
# Tutorial works well, need to verify if this will actually work headless on a Pi though
###############################################################################
# TODO: 
# - Verify headless functionality (https://stackoverflow.com/questions/25027385/using-selenium-on-raspberry-pi-headless)
###############################################################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Github credentials
username = "boogity"
password = ""

# initialize the Chrome driver
driver = webdriver.Chrome()

# Get the github login form
driver.get("https://github.com/login")
# Find username/password field, input relevant values
driver.find_element(By.ID, "login_field").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
# Submit your form and login
driver.find_element(By.NAME, "commit").click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors
for e in errors:
    print(e.text)
# if we find that error message within errors, report failure
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

driver.quit()