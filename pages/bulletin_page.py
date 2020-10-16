from .base_page import BasePage
from .locators import BulletinPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import time

class BulletinPage(BasePage):
    def add_new_bulletin_only_for (self, GSDB):
        self.browser.find_element(*BulletinPageLocators.ADD).click()
        self.browser.find_element(*BulletinPageLocators.SUBJECT).send_keys(GSDB)
        self.browser.find_element(*BulletinPageLocators.MESSAGE).send_keys(GSDB)
        self.browser.find_element(*BulletinPageLocators.FILTER_INPUT).send_keys(GSDB)
        self.browser.find_element(*BulletinPageLocators.FILTER_CHOICE).click()
        self.browser.find_element(*BulletinPageLocators.SUBMIT).click()

    def add_new_bulletin_with_attachment_only_for (self, GSDB, filename):
        self.browser.find_element(*BulletinPageLocators.ADD).click()
        self.browser.find_element(*BulletinPageLocators.SUBJECT).send_keys(GSDB)
        self.browser.find_element(*BulletinPageLocators.MESSAGE).send_keys(GSDB)
        self.browser.find_element(*BulletinPageLocators.FILTER_INPUT).send_keys(GSDB)
        self.browser.find_element(*BulletinPageLocators.FILTER_CHOICE).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, filename)
        self.browser.find_element(*BulletinPageLocators.ATTACH).send_keys(file_path)
        self.browser.find_element(*BulletinPageLocators.SUBMIT).click()

    def add_new_bulletin_for_everyone (self):
        self.browser.find_element(*BulletinPageLocators.ADD).click()
        self.browser.find_element(*BulletinPageLocators.SUBJECT).send_keys('All')
        self.browser.find_element(*BulletinPageLocators.MESSAGE).send_keys('All')
        self.browser.find_element(*BulletinPageLocators.SUBMIT).click()

    def add_new_bulletin_with_attachment_for_everyone (self, filename):
        self.browser.find_element(*BulletinPageLocators.ADD).click()
        self.browser.find_element(*BulletinPageLocators.SUBJECT).send_keys('All')
        self.browser.find_element(*BulletinPageLocators.MESSAGE).send_keys('All')
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, filename)
        self.browser.find_element(*BulletinPageLocators.ATTACH).send_keys(file_path)
        self.browser.find_element(*BulletinPageLocators.SUBMIT).click()

    def add_old_bulletin_only_for (self, GSDB):
        self.browser.find_element(*BulletinPageLocators.ADD).click()
        self.browser.find_element(*BulletinPageLocators.SUBJECT).send_keys(GSDB+'_old')
        self.browser.find_element(*BulletinPageLocators.DATE_FROM).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*BulletinPageLocators.DATE_FROM).send_keys("01/01/2020")
        self.browser.find_element(*BulletinPageLocators.DATE_TILL).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*BulletinPageLocators.DATE_TILL).send_keys("01/01/2020")
        self.browser.find_element(*BulletinPageLocators.MESSAGE).send_keys(GSDB+'_old')
        self.browser.find_element(*BulletinPageLocators.FILTER_INPUT).send_keys(GSDB)
        self.browser.find_element(*BulletinPageLocators.FILTER_CHOICE).click()
        self.browser.find_element(*BulletinPageLocators.SUBMIT).click()

    def add_old_bulletin_with_attachment_only_for (self, GSDB, filename):
        self.browser.find_element(*BulletinPageLocators.ADD).click()
        self.browser.find_element(*BulletinPageLocators.SUBJECT).send_keys(GSDB+'_old')
        self.browser.find_element(*BulletinPageLocators.DATE_FROM).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*BulletinPageLocators.DATE_FROM).send_keys("01/01/2020")
        self.browser.find_element(*BulletinPageLocators.DATE_TILL).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*BulletinPageLocators.DATE_TILL).send_keys("01/01/2020")
        self.browser.find_element(*BulletinPageLocators.MESSAGE).send_keys(GSDB+'_old')
        self.browser.find_element(*BulletinPageLocators.FILTER_INPUT).send_keys(GSDB)
        self.browser.find_element(*BulletinPageLocators.FILTER_CHOICE).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, filename)
        self.browser.find_element(*BulletinPageLocators.ATTACH).send_keys(file_path)
        self.browser.find_element(*BulletinPageLocators.SUBMIT).click()

    def add_old_bulletin_for_everyone (self):
        self.browser.find_element(*BulletinPageLocators.ADD).click()
        self.browser.find_element(*BulletinPageLocators.DATE_FROM).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*BulletinPageLocators.DATE_FROM).send_keys("01/01/2020")
        self.browser.find_element(*BulletinPageLocators.DATE_TILL).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*BulletinPageLocators.DATE_TILL).send_keys("01/01/2020")
        self.browser.find_element(*BulletinPageLocators.SUBJECT).send_keys('All_old')
        self.browser.find_element(*BulletinPageLocators.MESSAGE).send_keys('All_old')
        self.browser.find_element(*BulletinPageLocators.SUBMIT).click()

    def add_old_bulletin_with_attachment_for_everyone (self, filename):
        self.browser.find_element(*BulletinPageLocators.ADD).click()
        self.browser.find_element(*BulletinPageLocators.DATE_FROM).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*BulletinPageLocators.DATE_FROM).send_keys("01/01/2020")
        self.browser.find_element(*BulletinPageLocators.DATE_TILL).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*BulletinPageLocators.DATE_TILL).send_keys("01/01/2020")
        self.browser.find_element(*BulletinPageLocators.SUBJECT).send_keys('All_old')
        self.browser.find_element(*BulletinPageLocators.MESSAGE).send_keys('All_old')
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, filename)
        self.browser.find_element(*BulletinPageLocators.ATTACH).send_keys(file_path)
        self.browser.find_element(*BulletinPageLocators.SUBMIT).click()
    
    def clean_up_bulletins_list (self, browser):
        buttons = self.browser.find_elements(By.CSS_SELECTOR, ".mdi-delete")
        print(buttons)
        while len(buttons) > 0:
            for i in buttons:
                print(i)
                WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mdi-delete")))
                self.browser.execute_script("arguments[0].click();", self.browser.find_element(By.CSS_SELECTOR, ".mdi-delete"))
                self.browser.execute_script("arguments[0].click();", self.browser.find_element(By.XPATH, "//span[text()=' Delete ']"))
            buttons = self.browser.find_elements(By.CSS_SELECTOR, ".mdi-delete")

    def clean_up_bulletins_list2 (self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mdi-delete")))

        self.browser.execute_script("arguments[0].click();", self.browser.find_element(By.XPATH, "//span[text()=' Delete ']"))

    def check_bulletins_current_aurus(self, number):
        self.browser.find_element(*BulletinPageLocators.ALL_NEW)
        self.browser.find_element(*BulletinPageLocators.SUP01_NEW)
        self.browser.find_element(*BulletinPageLocators.SUP02_NEW)
        assert len(self.browser.find_elements(By.CSS_SELECTOR, ".v-card__title"))==number, "Filters work improperly"
    
    def go_to_past_bulletins(self):
        self.browser.find_element(*BulletinPageLocators.PAST).click()

    def check_bulletins_past_aurus(self, number):
        self.browser.find_element(*BulletinPageLocators.ALL_PAST)
        self.browser.find_element(*BulletinPageLocators.SUP01_PAST)
        self.browser.find_element(*BulletinPageLocators.SUP02_PAST)
        assert len(self.browser.find_elements(By.CSS_SELECTOR, ".v-card__title"))==number, "Filters work improperly"
    
    def modify_bulletin(self):
        self.browser.find_element(*BulletinPageLocators.PENCIL).click()
        time.sleep(5)
        self.browser.find_element(*BulletinPageLocators.MESSAGE_EDIT).send_keys('_edited')
        time.sleep(5)
        self.browser.find_element(*BulletinPageLocators.SUBMIT).click()
        time.sleep(5)
    
    def check_bulletins_sa (self):
        self.browser.find_element(
            *BulletinPageLocators.EMPTY_LIST)

