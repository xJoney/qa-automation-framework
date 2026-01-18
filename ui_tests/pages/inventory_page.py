from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def add_to_cart(self, item_name):
        button = self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        button.click()

    def remove_from_cart(self, item_name):
        button = self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        button.click()
    
    def cart_count(self):
        try:
            return int(self.driver.find_element(*self.cart_badge).text)
        except:
            return 0