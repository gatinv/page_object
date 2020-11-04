from .base_page import BasePage
from .locators import SuppliersPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import time

class SuppliersPage(BasePage):
    def open_supplier(self,ASDB):
        self.browser.find_element(By.XPATH, "//td[text() ='%s']/following-sibling::td/button"%ASDB).click()

    def modify_supplier(self,ASDB,address1,address2,address3,timezone,lang):
        self.browser.find_element(By.XPATH, "//td[text() ='%s']/following-sibling::td/button"%ASDB).click()
        self.browser.find_element(*SuppliersPageLocators.SHIPPING_ADDRESS).send_keys(address1)
        self.browser.find_element(*SuppliersPageLocators.PHYSICAL_ADDRESS).send_keys(address2)
        self.browser.find_element(*SuppliersPageLocators.BILLING_ADDRESS).send_keys(address3)
        self.browser.find_element(*SuppliersPageLocators.TIMEZONE).send_keys(timezone)
        self.browser.find_element(*SuppliersPageLocators.TIMEZONE).send_keys(Keys.ENTER)
        self.browser.find_element(*SuppliersPageLocators.LANG).click()
        self.browser.find_element(By.XPATH, "//div[contains(@class, 'menuable__content__active')]//div[text()='%s']"%lang).click()
        self.browser.find_element(*SuppliersPageLocators.SAVE).click()

    