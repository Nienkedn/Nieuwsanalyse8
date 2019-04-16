# Imports
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Settings
from selenium.webdriver.support.wait import WebDriverWait

headless = False
website_url = "https://www.facebook.com/"


# The main method of this file
def main():
    login(open_facebook())


# Opens the facebook website
def open_facebook():
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(website_url)

    # Wait until page is completely loaded
    while not page_has_loaded(browser):
        time.sleep(200)

    return browser


# Logs the user into facebook
def login(driver):
    driver.find_element_by_xpath("//input[@id='email']").send_keys("email@domain.com")
    driver.find_element_by_xpath("//input[@id='pass']").send_keys("password")
    driver.find_element_by_xpath("//input[@id='u_0_3']").click()


# Checks if the page has been loaded
def page_has_loaded(self):
    page_state = self.execute_script('return document.readyState;')
    return page_state == 'complete'


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
