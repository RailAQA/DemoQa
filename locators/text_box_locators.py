from selenium.webdriver.common.by import By


class TextBoxLocators:
    FULL_NAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    ADDRESS = (By.ID, 'currentAddress')
    DEFAULT_ADDRESS = (By.ID, 'permanentAddress')
    SUBMIT_BUTTON = (By.ID, 'submit')

    RESULT_TABLE = (By.ID, 'output')
    RESULTS_ALL = (By.XPATH, '//div[@class="border col-md-12 col-sm-12"]//p')
    