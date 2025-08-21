from pages.base_page import BasePage
from generator.generator import generated_form
from locators.text_box_locators import TextBoxLocators
locators = TextBoxLocators()


class TextBoxPage(BasePage):

    def scroll_to_fname_input(self):
        self.scroll_to(element=self.find(locators.FULL_NAME))
        self.element_is_visible(15, locators.FULL_NAME)

    def scroll_to_email_input(self):
        self.scroll_to(element=self.find(locators.EMAIL))
        self.element_is_visible(15, locators.EMAIL) 

    def scroll_to_caddress_input(self):
        self.scroll_to(element=self.find(locators.ADDRESS))
        self.element_is_visible(15, locators.ADDRESS) 

    def scroll_to_daddress_input(self):
        self.scroll_to(element=self.find(locators.DEFAULT_ADDRESS))
        self.element_is_visible(15, locators.DEFAULT_ADDRESS) 

    def form_filling(self):
        generator = next(generated_form())
        full_name = generator.full_name
        email = generator.email
        current_address = generator.address
        permanent_address = generator.default_address
        self.scroll_to_fname_input()
        self.find(locators.FULL_NAME).send_keys(full_name)
        self.scroll_to_email_input()
        self.find(locators.EMAIL).send_keys(email)
        self.scroll_to_caddress_input()
        self.find(locators.ADDRESS).send_keys(current_address)
        self.scroll_to_daddress_input()
        self.find(locators.DEFAULT_ADDRESS).send_keys(permanent_address)
        self.find(locators.SUBMIT_BUTTON).click()
        return [full_name, email, current_address, permanent_address]

    def form_result_is_visible(self):
        return self.assert_element_is_visible(locators.RESULT_TABLE)
    
    def scroll_to_result(self):
        self.scroll_to(element=self.find(locators.RESULT_TABLE))
        self.element_is_visible(15, locators.RESULT_TABLE)

    def scroll_to_send_button(self):
        self.scroll_to(element=self.find(locators.SUBMIT_BUTTON))
        self.element_is_visible(15, locators.SUBMIT_BUTTON)

    def results_data(self):
        return [i.text for i in self.finds(locators.RESULTS_ALL)]
    
    def send_empty_form(self):
        self.find(locators.SUBMIT_BUTTON).click()

    def form_result_not_visible(self):
        return self.assert_element_not_in_dom(locators.RESULTS_ALL)