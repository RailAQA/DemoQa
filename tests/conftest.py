from selenium import webdriver
import pytest
from generator.generator import generated_file
from pages.Elements.main_page import MainPage
from pages.Elements.links_page import LinksPage
from pages.Elements.forms_page import FormsPage
from pages.Elements.upload_page import UploadPage
from pages.Elements.buttons_page import ButtonsPage
from pages.Elements.text_box_page import TextBoxPage
from pages.Elements.check_box_page import CheckBoxPage
from pages.Elements.broken_links_page import BrokenLinksPage
from pages.Elements.radio_button_page import RadioButtonPage
from pages.Elements.properties_page import PropertiesPage
from pages.alerts_window.alerts_page import AlertsPage
random_file = generated_file()


@pytest.fixture(scope='function')
def driver():
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument(f'--proxy-server={"223.204.168.248:4153"}')
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

@pytest.fixture
def properties_page(driver):
    return PropertiesPage(driver)

@pytest.fixture
def alerts_page(driver):
    return AlertsPage(driver)

