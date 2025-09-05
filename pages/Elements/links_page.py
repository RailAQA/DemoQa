from pages.base_page import BasePage
from locators.elements.links_locators import LinksPageLocators
from generator.generator import generated_links, generated_links_result
locators = LinksPageLocators()

class LinksPage(BasePage):

    def scroll_to_following_links(self):
        self.scroll_to(element=self.find(locators.BAD_REQUEST_LINK))

    def click_to_following_link(self):
        generator = generated_links()
        self.find(generator).click()
        self.element_is_visible(15, locators.DATA_RESULT)
        if self.find(generator).text == "Created":
            self.choice = ["201", "Created"]
        elif self.find(generator).text == "No Content":
            self.choice = ["204", "No Content"]
        elif self.find(generator).text == "Moved":
            self.choice = ["301", "Moved Permanently"]
        elif self.find(generator).text == "Bad Request":
            self.choice = ["400", "Bad Request"]
        elif self.find(generator).text == "Unauthorized":
            self.choice = ["401", "Unauthorized"]
        elif self.find(generator).text == "Forbidden":
            self.choice = ["403", "Forbidden"]
        elif self.find(generator).text == "Not Found":
            self.choice = ["404", "Not Found"]

    def scroll_to_result(self):
        self.scroll_to(element=self.find(locators.DATA_RESULT))

    def check_data_result(self):
        results = [i.text for i in self.finds(locators.DATA_RESULT)]
        print(self.choice, results, sep="\n")
        if self.choice == results:
            return True
        else:
            return False