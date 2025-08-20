from pages.base_page import BasePage
from generator.generator import generated_person
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
        generator = next(generated_person())
        full_name = generator.first_name + generator.last_name
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

    def form_result_is_visible(self):
        return self.assert_element_is_visible(locators.RESULT_TABLE)