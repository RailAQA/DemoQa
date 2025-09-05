from selenium.webdriver.common.by import By



class ButtonsLocators:
    DOUBLE_CLICK_BUTTON = (By.ID, 'id="doubleClickBtn"')
    RIGHT_CLICK_BUTTON = (By.ID, 'id="rightClickBtn"')
    CLICK_ME_BUTTON = (By.ID, 'id="rightClickBtn"')
    ALL_BUTTONS = (By.XPATH, '//button[@type="button"][@class="btn btn-primary"]')
    TEXT_RESULT = (By.XPATH, "//p[contains(@id, 'ClickMessage')]")