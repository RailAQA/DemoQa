from pages.base_page import BasePage
from generator.generator import generated_button
from locators.buttons_locators import ButtonsLocators
from selenium.webdriver.common.action_chains import ActionChains
locators = ButtonsLocators()

class ButtonsPage(BasePage):

    def scroll_to_button(self):
        self.scroll_to(element=self.find(locators.RIGHT_CLICK_BUTTON))

    def click_button(self):
        actions = ActionChains(self.driver)
        generator = generated_button()
        if generator == 0:
            self.choice_button = "You have done a double click"
            actions.double_click(self.finds(locators.ALL_BUTTONS)[generator]).perform()
        elif generator == 0:
            self.choice_button = "You have done a right click"
            actions.context_click(self.finds(locators.ALL_BUTTONS)[generator]).perform()
        elif generator == 0:
            self.choice_button = "You have done a dynamic click"
            self.finds(locators.ALL_BUTTONS)[generator].click()

    def check_text_result(self):
        result = self.find(locators.TEXT_RESULT).text
        if self.choice_button == result:
            return True
        else:
            return False