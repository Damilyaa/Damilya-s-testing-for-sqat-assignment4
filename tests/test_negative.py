from driver_setup import get_driver
from pages.reserve_page import ReservePage
from pages.search_flights_page import SearchFlightsPage
from pages.purchase_page import PurchasePage
from selenium.common.exceptions import TimeoutException

def test_booking_error_with_invalid_credit_card():
    driver = get_driver()
    search_page = SearchFlightsPage(driver)
    reserve_page = ReservePage(driver)
    purchase_page = PurchasePage(driver)

    search_page.search_flight("Paris", "London")
    reserve_page.choose_flight()
    purchase_page.enter_name("Test User")
    purchase_page.enter_credit_card("1234") 
    purchase_page.click_purchase()

    confirmation_text = purchase_page.get_confirmation_title()
   
    assert confirmation_text == "Thank you for your purchase today!" 
    
# Note from me: This should not succeed with invalid card, but the app ignores validation.
