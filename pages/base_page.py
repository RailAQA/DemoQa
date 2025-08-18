from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, TimeoutException)
from locators.footer_locators import FooterLocators
footer_locators = FooterLocators()

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        try:
            self.element_is_clickable(15, footer_locators.LOGO_FOOTER)
        except TimeoutError:
            raise AssertionError(f"Страница {url} не прогрузилась")

    def element_is_clickable(self, timeout: int, args):
        wait(self.driver, timeout).until(EC.element_to_be_clickable(args))
    
    def scroll_to(self, element):
            self.driver.execute_script("return arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)

    def find(self, args):
         try:
            return self.driver.find_element(*args)
         except NoSuchElementException:
            raise AssertionError(f"Элемент с локатором {args} не существует в DOM")
         
    def assert_element_is_visible(self, args):
        return self.find(args).is_displayed()
    
    def opened_url_is(self, url):
        return self.driver.current_url == url

