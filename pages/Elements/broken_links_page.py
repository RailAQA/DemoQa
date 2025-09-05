from locators.elements.broken_links_locators import BrokenLinksLocators
from locators.elements.footer_locators import FooterLocators
from pages.base_page import BasePage
locators = BrokenLinksLocators()
locators_footer = FooterLocators()

class BrokenLinksPage(BasePage):
    def scroll_to_valid_image(self):
        self.scroll_to(element=self.find(locators.VALID_IMAGE))

    def check_valid_image(self):
        return self.assert_element_is_visible(locators.VALID_IMAGE)
    
    def scroll_to_broken_image(self):
        self.scroll_to(element=self.find(locators.BROKEN_IMAGE))

    def check_broken_image(self):
        #return self.assert_element_is_not_visible(locators.BROKEN_IMAGE)
        return self.assert_element_not_visible_with_wait(locators.BROKEN_IMAGE)
    
    def scroll_to_valid_link_button(self):
        self.scroll_to(element=self.find(locators.VALID_LINK))

    def click_to_valid_link(self):
        self.find(locators.VALID_LINK).click()
        self.element_is_clickable(15, locators_footer.LOGO_FOOTER)
    
    def scroll_to_broken_link_button(self):
        self.scroll_to(element=self.find(locators.BROKEN_LINK))

    def click_to_broken_link(self):
        self.find(locators.BROKEN_LINK).click()
