import configparser
from pages.search_flights_page import SearchFlightsPage
from pages.reserve_page import ReservePage
from pages.purchase_page import PurchasePage
from selenium import webdriver

def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://blazedemo.com/")
    return driver

def test_flight_booking_success():
    config = configparser.ConfigParser()
    config.read('test_data.ini')

    name = config['USER']['name']
    credit_card = config['USER']['credit_card']
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
    purchase_page.enter_credit_card(credit_card)
    purchase_page.hover_over_purchase_button() 
    purchase_page.press_tab_in_name_field()    
    purchase_page.click_purchase()
    confirmation_text = purchase_page.get_confirmation_title()
    assert confirmation_text == "Thank you for your purchase today!"
    driver.quit()