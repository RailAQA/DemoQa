from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.footer_locators import FooterLocators
main_locators = MainPageLocators()
footer_locators = FooterLocators()

class MainPage(BasePage):
    def main_page_is_opened(self):
        return self.assert_element_is_visible(main_locators.CARDS_MAIN_PAGE_CONTAINER)

    def scroll_to_elements_card(self):
        self.scroll_to(element=self.find(main_locators.CARDS_ELEMENTS))

    def click_to_elements_card(self):
        self.find(main_locators.CARDS_ELEMENTS).click()
        self.element_is_clickable(20, footer_locators.LOGO_FOOTER)

    