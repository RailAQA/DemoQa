from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from locators.alerts_window.alerts_locators import AlertsLocators
from generator.generator import generated_alert_acept
locators = AlertsLocators()


class AlertsPage(BasePage):
    

    def click_to_first_alert_button(self):
        self.find(locators.SEE_ALLERT_BUTTON).click()

    def click_to_timer_alert_button(self):
        self.find(locators.TIMER_BUTTON).click()

    def click_to_cofirm_button(self):
        self.find(locators.CONFIRM_BUTTON).click()


    def checker_alert_is_opened(self):
        try:
            self.alert_is_present_wait(5)
            self.driver.switch_to.alert
            print(f"Алерт открылся")
            return True
        except NoAlertPresentException:
            raise AssertionError(f"Алерт не открылся")
        
    def random_acepting_alert(self):
        generator = generated_alert_acept()
        if generator == 0:
            self.driver.switch_to.alert.accept()
            self.select_confirming = "Ok"
        else:
            self.driver.switch_to.alert.dismiss()
            self.select_confirming = "Cancel"

    def checker_alert_is_closed(self):
        try:
            self.alert_is_not_present_wait(5)
            return True
        except TimeoutException:
            print("Алерт не закрылся")
            return False

    def check_result_confirming_alert(self):
        result = self.find(locators.RESULT_CONFIRM_ALERT).text
        print(f'Выбран {self.select_confirming}, результат {result}')
        return self.select_confirming in result


