from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReservePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.CHOOSE_FLIGHT_BUTTON = (By.XPATH, "//input[@type='submit']")  

    def choose_flight(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//table[@class='table']")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Choose This Flight']"))).click()