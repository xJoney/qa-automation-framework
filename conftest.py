import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # chrome driver automatic install
    service = Service("/usr/bin/chromedriver")

    # setting up options for chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")

    # webdriver instance
    driver = webdriver.Chrome(service=service, options=options)

    # makes availble to test, quits browser after finished testing
    yield driver
    driver.quit()