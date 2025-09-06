from pages.base_page import BasePage
from locators.alerts_window.window_locators import WindowLocators
locators = WindowLocators()

class WindowPage(BasePage):

    def click_to_tab_button(self):
        """ Клик по кнопке "New Tab"  """
        self.current_tab = self.driver.window_handles.index(self.driver.current_window_handle)
        self.find(locators.TAB_BUTTON).click()

    def click_to_window_button(self):
        """ Клик по кнопке "New Window"  """
        self.find(locators.WINDOW_BUTTON).click()

    def check_new_tab(self):
        """ Проверяем, что открылась новая вкладка  """
        new_tab = self.driver.window_handles[self.current_tab + 1]
        self.driver.switch_to.window(new_tab)
        return self.element_is_visible(10, locators.NEW_TAB_TEXT).text == "This is a sample page"
    
    def check_new_window(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])
        return self.element_is_visible(15, locators.NEW_TAB_TEXT).text == 'This is a sample page'