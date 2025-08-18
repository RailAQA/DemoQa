from selenium import webdriver
import pytest
from pages.main_page import MainPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)