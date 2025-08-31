from pages.base_page import BasePage
from locators.upload_locators import UploadPageLocators
import os
from generator.generator import generated_new_file
locators = UploadPageLocators()
from time import sleep


class UploadPage(BasePage):
    def scroll_to_downlodad_button(self):
        self.scroll_to(element=self.find(locators.DOWNLOAD_BUTTON))

    def click_to_download_button(self):
        self.find(locators.DOWNLOAD_BUTTON).click()
        sleep(2)
        self.name_file = self.find(locators.DOWNLOAD_BUTTON).get_attribute("download")

    def check_file_is_saved(self):
        path = "/Users/ann/Downloads/" + self.name_file
        try:
            return os.path.exists(path)
        finally:
            self.delete_file(path=path)
        
    def scroll_to_upload_file_button(self):
        self.scroll_to(element=self.find(locators.SELECT_FILE_BUTTON))

    def upload_file(self):
        self.new__file_path, self.new_file = generated_new_file()
        self.find(locators.SELECT_FILE_BUTTON).send_keys(self.new__file_path)
        self.delete_file(path=self.new__file_path)
        
    def check_file_is_uploaded(self):
        self.element_is_visible(15, locators.FAKE_PATH)
        return self.find(locators.FAKE_PATH).text == "C:\\fakepath\\" + self.new_file + ".txt"
    
    def delete_file(self, path):
        if os.path.exists(path):
            os.remove(path)

