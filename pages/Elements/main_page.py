from pages.base_page import BasePage
from locators.elements.main_page_locators import MainPageLocators
from locators.elements.footer_locators import FooterLocators
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

    def scroll_to_forms_card(self):
        self.scroll_to(element=self.find(main_locators.CARDS_FORMS))
    
    def click_to_forms_card(self):
        self.find(main_locators.CARDS_FORMS).click()
        self.element_is_clickable(20, footer_locators.LOGO_FOOTER)

    def scroll_to_alerts_card(self):
        self.scroll_to(element=self.find(main_locators.CARDS_ALERTS))

    def click_to_alerts_card(self):
        self.find(main_locators.CARDS_ALERTS).click()
        self.element_is_clickable(20, footer_locators.LOGO_FOOTER)

    def scroll_to_widgets_card(self):
        self.scroll_to(element=self.find(main_locators.CARDS_WIDGETS))

    def click_to_widgets_card(self):
        self.find(main_locators.CARDS_WIDGETS).click()
        self.element_is_clickable(20, footer_locators.LOGO_FOOTER)
    
    def scroll_to_interactions_card(self):
        self.scroll_to(element=self.find(main_locators.CARDS_INTERACTIONS))

    def click_to_interactions_card(self):
        self.find(main_locators.CARDS_INTERACTIONS).click()
        self.element_is_clickable(20, footer_locators.LOGO_FOOTER)

    def scroll_to_books_card(self):
        self.scroll_to(element=self.find(main_locators.CARDS_BOOK))

    def click_to_books_card(self):
        self.find(main_locators.CARDS_BOOK).click()
        self.element_is_clickable(20, footer_locators.LOGO_FOOTER)