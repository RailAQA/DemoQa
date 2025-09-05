from selenium.webdriver.common.by import By


class AlertsLocators:
    SEE_ALLERT_BUTTON = (By.ID, 'alertButton')
    TIMER_BUTTON = (By.ID, 'timerAlertButton')
    CONFIRM_BUTTON = (By.ID, 'confirmButton')
    RESULT_CONFIRM_ALERT = (By.ID, 'confirmResult')
    PROMT_BUTTON = (By.ID, 'promtButton')
    PROMT_RESULT = (By.ID, 'promptResult')