from .base_page import BasePage
from .locators import ASNPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class ASNPage(BasePage):
    def createASN (self, carrier, plant, container, trans, shipDate, bol, freight, netW, grossW, contract, part, qty, total, uom, partW, origin, qty_pack, level3, level2, level1, tareW):
        self.browser.find_element(*ASNPageLocators.CREATE).click()
        self.browser.find_element(*ASNPageLocators.CARRIER).send_keys(carrier)
        self.browser.find_element(*ASNPageLocators.PLANTLIST).click()
        self.browser.find_element(By.XPATH, "//div[text()='%s']"%plant).click()
        self.browser.find_element(*ASNPageLocators.CONTAINER).send_keys(container)
        self.browser.find_element(*ASNPageLocators.TRANS).send_keys(trans)
        self.browser.find_element(*ASNPageLocators.SHIP_DATE).send_keys(shipDate)
        self.browser.find_element(*ASNPageLocators.BOL).send_keys(bol)
        self.browser.find_element(*ASNPageLocators.FREIGHT).send_keys(freight)
        self.browser.find_element(*ASNPageLocators.NET_WEIGHT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*ASNPageLocators.NET_WEIGHT).send_keys(netW)
        self.browser.find_element(*ASNPageLocators.GROSS_WEIGHT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*ASNPageLocators.GROSS_WEIGHT).send_keys(grossW)
        self.browser.find_element(*ASNPageLocators.CONTRACT).send_keys(contract)
        self.browser.find_element(*ASNPageLocators.ADD_PARTS).click()
        self.browser.find_element(*ASNPageLocators.PARTS_PART).send_keys(part)
        self.browser.find_element(*ASNPageLocators.PARTS_QTY).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*ASNPageLocators.PARTS_QTY).send_keys(qty)
        self.browser.find_element(*ASNPageLocators.PARTS_TOTAL).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*ASNPageLocators.PARTS_TOTAL).send_keys(total)
        self.browser.find_element(*ASNPageLocators.PARTS_UOM).send_keys(uom)
        self.browser.find_element(*ASNPageLocators.PARTS_WEIGHT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*ASNPageLocators.PARTS_WEIGHT).send_keys(partW)
        self.browser.find_element(*ASNPageLocators.PARTS_ORIGIN).send_keys(origin)
        self.browser.find_element(*ASNPageLocators.PARTS_SUBMIT).click()
        self.browser.find_element(*ASNPageLocators.ADD_PACKS).click()
        self.browser.find_element(*ASNPageLocators.PACKS_PART).send_keys(part)
        self.browser.find_element(*ASNPageLocators.PACKS_QTY).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*ASNPageLocators.PACKS_QTY).send_keys(qty_pack)
        self.browser.find_element(*ASNPageLocators.PACKS_LEVEL3).send_keys(level3)
        self.browser.find_element(*ASNPageLocators.PACKS_LEVEL2).send_keys(level2)
        self.browser.find_element(*ASNPageLocators.PACKS_LEVEL1).send_keys(level1)
        self.browser.find_element(*ASNPageLocators.PACKS_TARE).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*ASNPageLocators.PACKS_TARE).send_keys(tareW)
        self.browser.find_element(*ASNPageLocators.PACKS_SUBMIT).click()
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.browser.find_element(*ASNPageLocators.SUBMIT).click()
        time.sleep(2)

