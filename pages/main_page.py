from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):
    def go_to_bulletins_board(self):
        self.browser.find_element(*MainPageLocators.BULLETINS).click()
        self.browser.find_element(*MainPageLocators.BULLETINS_BOARD).click()

    def go_to_bulletins_list(self):
        self.browser.find_element(*MainPageLocators.BULLETINS).click()
        self.browser.find_element(*MainPageLocators.BULLETINS_LIST).click()

    def go_to_users(self):
        self.browser.find_element(*MainPageLocators.USERS).click()
