from selenium import webdriver
import pytest
from pages.main_page import MainPage
from pages.forms_page import FormsPage
from pages.text_box_page import TextBoxPage
from pages.check_box_page import CheckBoxPage



@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def forms_page(driver):
    return FormsPage(driver)

@pytest.fixture
def text_box_page(driver):
    return TextBoxPage(driver)

@pytest.fixture
def check_box_page(driver):
    return CheckBoxPage(driver)