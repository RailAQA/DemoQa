from selenium.webdriver.common.by import By


class RadioButtonLocators:

    RADIO_BUTTON_ALL = (By.XPATH, '//input[@class="custom-control-input"]')
    RESULT_TEXT = (By.XPATH, '//span[@class="text-success"]')