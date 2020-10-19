from .base_page import BasePage
from .locators import UsersPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time

class UsersPage(BasePage):
    def add_user (self, Email, Name, Role, GSDB):
        self.browser.find_element(*UsersPageLocators.ADD).click()
        self.browser.find_element(*UsersPageLocators.EMAIL).send_keys(Email)
        self.browser.find_element(*UsersPageLocators.NAME).send_keys(Name)
        self.browser.find_element(*UsersPageLocators.ROLES_LIST).click()
        self.browser.find_element(By.XPATH, "//div[text()='%s']"%Role).click()
        self.browser.find_element(*UsersPageLocators.GSDB).send_keys(GSDB)
        self.browser.find_element(*UsersPageLocators.SUBMIT).click()

    def modify_user (self, email, author):
        self.browser.find_element(By.XPATH, "//td[text() ='%s']/following-sibling::td/button"%email).click()
        self.browser.find_element(*UsersPageLocators.NAME).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*UsersPageLocators.NAME).send_keys("Edited by %s"%author)
        self.browser.find_element(*UsersPageLocators.SUBMIT).click()

    def check_user_row (self, browser, email):
        try:
            browser.find_element(By.XPATH, "//td[text()='%s']"%email)
            print('Checked successfully.')
        except:
            print('Refreshing..')
            browser.refresh()
            try:
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//td[text()='%s']"%email)))
                print('Checked successfully.')
            except Exception as e:
                print('Too bad.. The check failed.')
                print(e)
                now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                browser.get_screenshot_as_file('screenshot-%s.png' % now)