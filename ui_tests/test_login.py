from pages.login_page import LoginPage
import time

def test_valid_login(driver):
    login_page = LoginPage(driver)

    # open saucedemo and logs in 
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # testing to see how automation looks like
    # time.sleep(15)

    assert "inventory" in driver.current_url, "Login failed"
