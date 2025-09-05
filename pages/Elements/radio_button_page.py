from pages.base_page import BasePage
from locators.elements.radio_button_locators import RadioButtonLocators
from generator.generator import generated_radio_button
locators = RadioButtonLocators()

class RadioButtonPage(BasePage):

    def scroll_to_radio_button(self):
        self.scroll_to(element=self.find(locators.RADIO_BUTTON_ALL))

    def click_to_radio_button(self):
        generator = generated_radio_button()
        print(generator)
        self.script_click(element=self.finds(locators.RADIO_BUTTON_ALL)[generator])
        if generator == 0:
            self.radio = "Yes"
        else:
            self.radio = "Impressive"

    def check_result_text(self):
        self.element_is_visible(10, locators.RESULT_TEXT)
        result_text = self.find(locators.RESULT_TEXT).text
        if self.radio == result_text:
            return True
        else:
            return False