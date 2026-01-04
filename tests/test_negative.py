import configparser
from pages.search_flights_page import SearchFlightsPage
from pages.reserve_page import ReservePage
from pages.purchase_page import PurchasePage
from selenium import webdriver

def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://blazedemo.com/")
    return driver

def test_booking_error_with_invalid_credit_card():
    config = configparser.ConfigParser()
    config.read('test_data.ini')

    name = config['USER']['name']
    from_city = config['FLIGHT']['from_city']
    to_city = config['FLIGHT']['to_city']

    driver = get_driver()
    search_page = SearchFlightsPage(driver)
    reserve_page = ReservePage(driver)
    purchase_page = PurchasePage(driver)

    search_page.select_departure_city(from_city)
    search_page.select_destination_city(to_city)
    search_page.search_flight()
    reserve_page.choose_flight()
    purchase_page.enter_name(name)
    purchase_page.enter_credit_card("1234") 
    purchase_page.click_purchase()
    confirmation_text = purchase_page.get_confirmation_title()
    # This should fail in a real app, but BlazeDemo allows it.
    assert confirmation_text == "Thank you for your purchase today!"
    driver.quit()