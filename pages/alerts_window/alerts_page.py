from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from locators.alerts_window.alerts_locators import AlertsLocators
locators = AlertsLocators()


class AlertsPage(BasePage):
    

    def click_to_first_alert_button(self):
        self.find(locators.SEE_ALLERT_BUTTON).click()

    def checker_alert_is_opened(self):
        try:
            self.alert_is_present_wait(5)
            self.driver.switch_to.alert
            return True
        except NoAlertPresentException:
            raise AssertionError(f"Алерт не открылся")

