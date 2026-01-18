from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

# LOGIN TESTS-----------------------------------
def test_valid_login(driver):
    login_page = LoginPage(driver)

    # open saucedemo and logs in 
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # testing to see how automation looks like
    # time.sleep(15)

    assert "inventory" in driver.current_url, "Login failed"

def test_invalid_login(driver):
    login_page = LoginPage(driver)

    # open saucedemo and logs in with wrong info
    login_page.open()
    login_page.login("user", "password123")
    assert login_page.get_error_message() != ""


# ADD/REMOVE ITEM FROM CART TESTS------------------------------
def test_add_to_cart(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")

    assert inventory_page.cart_count() == 1

def test_remove_from_cart(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.remove_from_cart("Sauce Labs Backpack")

    assert inventory_page.cart_count() == 0

