from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchFlightsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_departure_city(self, city):
        select = Select(self.wait.until(EC.presence_of_element_located((By.NAME, "fromPort"))))
        select.select_by_visible_text(city)

    def select_destination_city(self, city):
        select = Select(self.wait.until(EC.presence_of_element_located((By.NAME, "toPort"))))
        select.select_by_visible_text(city)

    def search_flight(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))).click()