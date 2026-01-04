from driver_setup import get_driver
from pages.search_flights_page import SearchFlightsPage
from pages.reserve_page import ReservePage
from pages.purchase_page import PurchasePage

def test_flight_booking_success():
    driver = get_driver()

    search_page = SearchFlightsPage(driver)
    reserve_page = ReservePage(driver)
    purchase_page = PurchasePage(driver)

    search_page.search_flight("Paris", "London")
    reserve_page.choose_flight()
    purchase_page.enter_name("Damilya")
    purchase_page.click_purchase()

    confirmation_text = purchase_page.get_confirmation_title()
    assert confirmation_text == "Thank you for your purchase today!"

    driver.quit()
