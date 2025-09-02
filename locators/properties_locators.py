from selenium.webdriver.common.by import By


class PropertiesLocators:
    WILL_ENABLE_BUTTON = (By.ID, 'enableAfter')
    COLOR_CHANGE_BUTTON = (By.ID, 'colorChange')
    COLOR_BUTTON_AFTER_CHANGE = (By.CSS_SELECTOR, '[class="mt-4 text-danger btn btn-primary"]')
    VISIBLE_AFTER_5_SECONDS_BUTTON = (By.ID, 'visibleAfter')