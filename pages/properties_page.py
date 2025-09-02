from pages.base_page import BasePage
from locators.properties_locators import PropertiesLocators
from time import sleep
locators = PropertiesLocators()

class PropertiesPage(BasePage):
    def open(self, url):
        self.driver.get(url)

    def color_button_changing_color(self):
        self.element_is_present(10, locators.COLOR_BUTTON_AFTER_CHANGE)
        return self.find(locators.COLOR_CHANGE_BUTTON).value_of_css_property("color") == "rgba(220, 53, 69, 1)"
    
    def new_button_visible(self):
        self.element_is_present(10, locators.VISIBLE_AFTER_5_SECONDS_BUTTON)
        return self.assert_element_is_visible(locators.VISIBLE_AFTER_5_SECONDS_BUTTON)
    