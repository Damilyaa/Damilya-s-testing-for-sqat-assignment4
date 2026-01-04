
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class SearchFlightsPage(BasePage):

    FROM_CITY = (By.NAME, "fromPort")
    TO_CITY = (By.NAME, "toPort")
    FIND_FLIGHTS_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def search_flight(self, from_city, to_city):
        Select(self.wait_for_visibility(self.FROM_CITY)).select_by_visible_text(from_city)
        Select(self.wait_for_visibility(self.TO_CITY)).select_by_visible_text(to_city)
        self.wait_for_clickable(self.FIND_FLIGHTS_BUTTON).click()
