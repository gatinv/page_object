from selenium.webdriver.common.by import By


class LoginPageLocators():
    LANG = (By.CSS_SELECTOR, "input[type='hidden']")
    LOGIN = (By.CSS_SELECTOR, "#login")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    SIGN_IN = (By.CSS_SELECTOR, ".btn")

class MainPageLocators():
    BULLETINS = (By.XPATH, "//span[contains(.,'Bulletins')]")
    BULLETINS_BOARD = (By.XPATH, "//a[contains(.,'Bulletin board')]")
    BULLETINS_LIST = (By.XPATH, "//a[contains(.,'Bulletin list management')]")
    USERS = (By.XPATH, "//a[contains(.,'Users')]")

class BulletinPageLocators():
    ADD = (By.CSS_SELECTOR, "a.btn")
    SUBJECT = (By.XPATH, "//label[text()='Subject']/following-sibling::div//input")
    MESSAGE = (By.XPATH, "//label[text()='Message']/following-sibling::div//textarea")
    FILTER_INPUT = (By.XPATH, "//label[text()=' Supplier list ']/following-sibling::div//input[@type='text']")
    FILTER_CHOICE = (By.XPATH, "//span[@class='v-list-item__mask']")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    ATTACH = (By.CSS_SELECTOR, ".d-none")
    DATE_FROM = (By.XPATH, "//label[text()='Date (UTC)']/following-sibling::div//input")
    DATE_TILL = (By.XPATH, "//label[text()='Valid till (UTC)']/following-sibling::div//input")
    TRASH_BUTTON = (By.CSS_SELECTOR, ".mdi-delete")
    DELETE_BUTTON = (By.XPATH, "//span[text()=' Delete ']")
    ALL_NEW = (By.XPATH, "//div[text()=' All ']")
    SUP01_NEW = (By.XPATH, "//div[text()=' SUP01 ']")
    SUP02_NEW = (By.XPATH, "//div[text()=' SUP02 ']")
    PAST = (By.XPATH, "//span[text()=' Past ']")
    ALL_PAST = (By.XPATH, "//div[text()=' All_old ']")
    SUP01_PAST = (By.XPATH, "//div[text()=' SUP01_old ']")
    SUP02_PAST = (By.XPATH, "//div[text()=' SUP02_old ']")
    PENCIL = (By.CSS_SELECTOR, ".mdi-pencil")
    MESSAGE_EDIT = (By.XPATH, "//label[text()=' Message ']/following-sibling::div//textarea")
    EMPTY_LIST = (By.XPATH, "//div[text()='No data available']")

class UsersPageLocators():
    ADD = (By.XPATH, "//span[text()=' Add ']")
    EMAIL = (By.XPATH, "//label[text()='E-mail']/following-sibling::div//input")
    NAME = (By.XPATH, "//label[text()=' Name ']/following-sibling::div//input")
    ROLES_LIST = (By.XPATH, "//label[text()=' Role ']/following-sibling::div//i")
    GSDB = (By.XPATH, "//label[text()=' GSDB ']/following-sibling::div//input")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    USERS_LIST = (By.XPATH, "//table/tbody/tr")
    