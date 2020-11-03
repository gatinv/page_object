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
    
    def sign_out(self):
        self.browser.find_element(*MainPageLocators.PROFILE_DROP).click()
        self.browser.find_element(*MainPageLocators.SIGN_OUT).click()

    def go_to_ASN(self):
        self.browser.find_element(*MainPageLocators.ASN).click()

    def go_to_versions(self):
        self.browser.find_element(*MainPageLocators.VERSIONS).click()

    def go_to_suppliers(self):
        self.browser.find_element(*MainPageLocators.SUPPLIERS).click()

    def go_to_roles(self):
        self.browser.find_element(*MainPageLocators.ROLES).click()
    
    def go_to_email_archieve(self):
        self.browser.find_element(*MainPageLocators.EMAILS).click()
        self.browser.find_element(*MainPageLocators.EMAIL_ARCHIVE).click()

    def go_to_email_templates(self):
        self.browser.find_element(*MainPageLocators.EMAILS).click()
        self.browser.find_element(*MainPageLocators.EMAIL_TEMPLATES).click()

    def go_to_logs(self):
        self.browser.find_element(*MainPageLocators.LOGS).click()

    def go_to_orders_grouped_by_day(self):
        self.browser.find_element(*MainPageLocators.ORDERS).click()
        self.browser.find_element(*MainPageLocators.ORDERS_BY_DAY).click()

    def go_to_orders_nearest_date(self):
        self.browser.find_element(*MainPageLocators.ORDERS).click()
        self.browser.find_element(*MainPageLocators.NEAREST).click()

    def go_to_orders_nearest_by_supplier(self):
        self.browser.find_element(*MainPageLocators.ORDERS).click()
        self.browser.find_element(*MainPageLocators.NEAREST_BY_SUPP).click()

    def go_to_orders_12_months_by_part(self):
        self.browser.find_element(*MainPageLocators.ORDERS).click()
        self.browser.find_element(*MainPageLocators.TWELVE_BY_PART).click()

    def go_to_orders_12_months_by_parts(self):
        self.browser.find_element(*MainPageLocators.ORDERS).click()
        self.browser.find_element(*MainPageLocators.TWELVE_BY_PARTS).click()

    def go_to_orders_history_14_days(self):
        self.browser.find_element(*MainPageLocators.ORDERS).click()
        self.browser.find_element(*MainPageLocators.HISTORY_14).click()

    def go_to_orders_history_17_weeks(self):
        self.browser.find_element(*MainPageLocators.ORDERS).click()
        self.browser.find_element(*MainPageLocators.HISTORY_17).click()

    def go_to_orders_corrections(self):
        self.browser.find_element(*MainPageLocators.ORDERS).click()
        self.browser.find_element(*MainPageLocators.CORRECTIONS).click()

    def go_to_AS_orders(self):
        self.browser.find_element(*MainPageLocators.AS_ORDERS).click()

    def go_to_reports_transactions(self):
        self.browser.find_element(*MainPageLocators.REPORTS).click()
        self.browser.find_element(*MainPageLocators.TRANSACTIONS).click()

    def go_to_reports_turnover(self):
        self.browser.find_element(*MainPageLocators.REPORTS).click()
        self.browser.find_element(*MainPageLocators.TURNOVER).click()

    def go_to_reports_balance(self):
        self.browser.find_element(*MainPageLocators.REPORTS).click()
        self.browser.find_element(*MainPageLocators.BALANCE).click()

    def go_to_reports_forecasts(self):
        self.browser.find_element(*MainPageLocators.REPORTS).click()
        self.browser.find_element(*MainPageLocators.FORECASTS).click()

    def go_to_reports_parts_properties(self):
        self.browser.find_element(*MainPageLocators.REPORTS).click()
        self.browser.find_element(*MainPageLocators.PARTS_PROPERTIES).click()

    def go_to_reports_new_parts(self):
        self.browser.find_element(*MainPageLocators.REPORTS).click()
        self.browser.find_element(*MainPageLocators.NEW_PARTS).click()

    def go_to_reports_missing_parts(self):
        self.browser.find_element(*MainPageLocators.REPORTS).click()
        self.browser.find_element(*MainPageLocators.MISSING_PARTS).click()

    def go_to_label_printing(self):
        self.browser.find_element(*MainPageLocators.LABELS).click()
        self.browser.find_element(*MainPageLocators.LABEL_PRINTING).click()

    def go_to_label_template(self):
        self.browser.find_element(*MainPageLocators.LABELS).click()
        self.browser.find_element(*MainPageLocators.LABEL_TEMPLATE).click()
