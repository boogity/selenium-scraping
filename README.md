# About
Test repo to better understand using Selenium for webscraping. 
Stuck trying to figure out how to webscrape metrics from the Sierra Wireless RV55 LTE hot spot. 
I think this is due to too much Javascript on the backend. Hopefully using Selenium will simplify this.

# Dependencies
## Python Modules
pip3 install -r requirements.txt

## Web Browser Driver
You should no longer need to manually download a browser driver for Selenium to work, it should do it for you as of 4.6+
https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#use-the-latest-version-of-selenium

## Web Browser
You will still need a browser though. I'll be using google-chrome throughout this as it's what the web browser driver is searching for.
- Download debian, install package
- Ensure google-chrome binary is in your $PATH
