import pytest
from selenium import webdriver
from data import Data
from pages.home_page import HomePage
from pages.order_page import OrderFormPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Data.MAIN_PAGE_URL)

    yield driver

    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def order_page(driver):
    return OrderFormPage(driver)



