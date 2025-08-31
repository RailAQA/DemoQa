from selenium import webdriver
import pytest
import os
from generator.generator import generated_file
from pages.main_page import MainPage
from pages.links_page import LinksPage
from pages.forms_page import FormsPage
from pages.buttons_page import ButtonsPage
from pages.text_box_page import TextBoxPage
from pages.check_box_page import CheckBoxPage
from pages.broken_links_page import BrokenLinksPage
from pages.radio_button_page import RadioButtonPage
from pages.upload_page import UploadPage
random_file = generated_file()


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

@pytest.fixture
def radio_button_page(driver):
    return RadioButtonPage(driver)

@pytest.fixture
def buttons_page(driver):
    return ButtonsPage(driver)

@pytest.fixture
def links_page(driver):
    return LinksPage(driver)

@pytest.fixture
def broken_links_page(driver):
    return BrokenLinksPage(driver)

@pytest.fixture
def upload_page(driver):
    return UploadPage(driver)