from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, TimeoutException)
from locators.footer_locators import FooterLocators
import requests
footer_locators = FooterLocators()

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)
        try:
            self.element_is_visible(30, footer_locators.LOGO_FOOTER)
        except TimeoutError:
            raise AssertionError(f"Страница {url} не прогрузилась")
        except TimeoutException:
            raise AssertionError(f'Страница не загрузилась. Ответ сервера {requests.get(url).status_code}')

    def element_is_clickable(self, timeout: int, args):
        wait(self.driver, timeout).until(EC.element_to_be_clickable(args))

    def element_is_visible(self, timeout: int, args):
        wait(self.driver, timeout).until(EC.visibility_of_element_located(args))

    def element_is_not_visible(self, timeout: int, args: tuple):
        try:
            wait(self.driver, timeout).until_not(EC.visibility_of_element_located(args))
        except TimeoutException:
            raise AssertionError(f'Элемент с локатором {args} не стал невидимым')
    
    def scroll_to(self, element):
            self.driver.execute_script("return arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)

    def find(self, args):
         try:
            return self.driver.find_element(*args)
         except NoSuchElementException:
            raise AssertionError(f"Элемент с локатором {args} не существует в DOM")
         
    def element_is_present(self, timeout: int, args: tuple):
        """Ожидает, пока элемент появится в DOM, и возвращает его."""
        
        try:
            return wait(self.driver, timeout).until(EC.presence_of_element_located(args))
        except TimeoutError:
            raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не появился в DOM. Метод 'element_is_present'.")
        except TimeoutException:
            raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не появился в DOM. Метод 'element_is_present'.")
         
    def finds(self, args):
         try:
            return self.driver.find_elements(*args)
         except NoSuchElementException:
            raise AssertionError(f"Элемент с локатором {args} не существует в DOM")
         
    def assert_element_is_visible(self, args):
        return self.find(args).is_displayed()
    
    def assert_element_is_not_visible(self, args):
        return not self.find(args).is_displayed()
    
    def assert_element_not_in_dom(self, args):
        try:
            self.element_is_present(10, args)
            return False
        except AssertionError:
            return True
        
    def assert_element_not_visible_with_wait(self, args):
        try:
            self.element_is_visible(5, args)
            return False
        except TimeoutError:
            return True
        except TimeoutException:
            return True
    
    def opened_url_is(self, url):
        return url in self.driver.current_url
    
    def opened_url_is_not(self, url):
        return self.driver.current_url != url

    def script_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def alert_is_present_wait(self, timeout: int):
        return wait(self.driver, timeout).until(EC.alert_is_present()) # Без локатора т.к алерт
    
    def alert_is_not_present_wait(self, timeout: int):
        return wait(self.driver, timeout).until_not(EC.alert_is_present()) # Без локатора т.к алерт