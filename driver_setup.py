from selenium import webdriver

def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://blazedemo.com")
    return driver
