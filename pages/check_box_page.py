from pages.base_page import BasePage
from generator.generator import generated_check_box
from locators.check_box_locators import CheckBoxLocators
locators = CheckBoxLocators()

class CheckBoxPage(BasePage):

    def scroll_to_checkbox_block(self):
        self.scroll_to(element=self.find(locators.HOME_TOGGLE_BUTTON))

    def open_list(self):
        self.find(locators.HOME_TOGGLE_BUTTON).click()

    def check_list_is_opened(self):
        self.element_is_visible(10, locators.ALL_TOGGLES_SUBPARENT)
        return self.assert_element_is_visible(locators.ALL_CHECK_BOX_SUBPARENT)
    
    def click_to_check_box(self):
        random_locator = generated_check_box()
        self.find(random_locator).click()
        if random_locator == locators.DESKTOP_CHECKBOX:
            self.choice = "desktop notes commands"
        elif random_locator == locators.DOCUMENTS_CHECKBOX:
            self.choice = "documents workspace react angular veu office public private classified general"
        elif random_locator == locators.DOWNLOADS_CHECKBOX:
            self.choice = "downloads wordFile excelFile"
    
    def check_result(self):
        self.find(locators.TEXT_RESULTS)
        result =  " ".join([i.text for i in self.finds(locators.TEXT_RESULTS)])
        if self.choice == result:
            return True
        else:
            return False
