from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PurchasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.PURCHASE_BUTTON = (By.XPATH, "//input[@value='Purchase Flight']")
        self.NAME_INPUT = (By.ID, "inputName")
        self.CONFIRMATION_TITLE = (By.TAG_NAME, "h1")

    def enter_name(self, name):
        self.wait.until(EC.presence_of_element_located(self.NAME_INPUT)).send_keys(name)

    def click_purchase(self):
        self.wait.until(EC.element_to_be_clickable(self.PURCHASE_BUTTON)).click()

    def get_confirmation_title(self):
        return self.wait.until(EC.presence_of_element_located(self.CONFIRMATION_TITLE)).text
    