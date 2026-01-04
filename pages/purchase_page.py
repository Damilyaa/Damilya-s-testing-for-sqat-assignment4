from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class PurchasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_name(self, name):
        self.wait.until(EC.presence_of_element_located((By.ID, "inputName"))).send_keys(name)

    def enter_credit_card(self, card_number):
        self.wait.until(EC.presence_of_element_located((By.ID, "creditCardNumber"))).send_keys(card_number)

    def click_purchase(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Purchase Flight']"))).click()

    def get_confirmation_title(self):
        return self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text

    def hover_over_purchase_button(self):
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Purchase Flight']")))
        ActionChains(self.driver).move_to_element(button).perform()

    def press_tab_in_name_field(self):
        name_input = self.wait.until(EC.presence_of_element_located((By.ID, "inputName")))
        name_input.send_keys(Keys.TAB)

    def switch_to_new_window(self):
        main_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

    def switch_to_iframe(self, iframe_id):
        self.driver.switch_to.frame(iframe_id)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()