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
from bs4 import BeautifulSoup
# Only need this to access OS environment variables for secrets
import os

# Github credentials
username = "boogity"
# ->$ export GITHUB_PASSWORD='<your github password>'
password = os.getenv('GITHUB_PASSWORD')

# initialize the Chrome driver
driver = webdriver.Chrome()

###############################################################################
#                               LOGIN TO GITHUB
###############################################################################
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

###############################################################################
#                         ACCESS PRIVILEGED PAGE
###############################################################################

print("You'll want to use driver.page_source to access to HTML for the page.")
print("You should use BS4 html parser in conjunction with the raw html of driver.page_source")


# Testing whether soup is needed at all, looks like the formatting is much nicer in soup
# Do we care about the format if we're just looking to grep specific values though?
driver.get("https://github.com/settings/keys")
with open("sel.html", "a") as f:
    print(driver.page_source, file=f)
    print("Output raw html from driver.page_source to ./sel.html")

with open("soup.html", "a") as f:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    print(soup.prettify(), file=f)
    print("Output the prettified HTML from BS4's parsing of the raw HTML to ./soup.html")



driver.quit()