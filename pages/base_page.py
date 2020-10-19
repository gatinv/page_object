from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

os.environ['apiurl']="https://api-250.aurus-sp.app/api"
os.environ['spurl']="https://250.aurus-sp.app/sign-in"

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = os.environ.get('spurl')
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)

    def wait_for_alert (self, browser):
        try:
            WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'toast-body')))
            print("alert!")
        except TimeoutException:
            print("Seems like we are safe...")
            time.sleep(1)
            print("..for now")

