from driver_setup import get_driver
from pages.reserve_page import ReservePage
from selenium.common.exceptions import TimeoutException

def test_cannot_choose_flight_without_search():
    driver = get_driver()
    reserve_page = ReservePage(driver)

    try:
        reserve_page.choose_flight()
        booked = True
    except TimeoutException:
        booked = False

    assert booked is False, "Should not be able to choose a flight before searching"
