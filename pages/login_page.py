from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()

    def choose_english_as_default_language(self):
        language = "en"
        lang = self.browser.find_element(*LoginPageLocators.LANG).get_attribute("value")
        if (language == lang):
            pass
        else:
            self.browser.find_element_by_css_selector(".v-select__slot .v-icon").click()
            self.browser.find_element_by_css_selector(".v-list [aria-selected='false']").click()

    def choose_russian_as_default_language(self):
        language = "ru"
        lang = self.browser.find_element(*LoginPageLocators.LANG).get_attribute("value")
        if (language == lang):
            pass
        else:
            self.browser.find_element_by_css_selector(".v-select__slot .v-icon").click()
            self.browser.find_element_by_css_selector(".v-list [aria-selected='false']").click()
    
    def login_as (self, username, password):
        self.browser.find_element(*LoginPageLocators.LOGIN).send_keys(username)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SIGN_IN).click()
