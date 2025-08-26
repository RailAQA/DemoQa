from selenium.webdriver.common.by import By


class LinksPageLocators:
    HOME_LINK = (By.ID, 'simpleLink')
    HOME6HFD4 = (By.ID, 'dynamicLink')

    CREATED_LINK = (By.ID, 'created')
    NO_CREATED_LINK = (By.ID, 'no-content')
    MOVED_LINK = (By.ID, 'moved')
    BAD_REQUEST_LINK = (By.ID, 'bad-request')
    UNAUTH_LINK = (By.ID, 'unauthorized')
    FORBIDDEN_LINK = (By.ID, 'forbidden')
    NOT_FOUND_LINK = (By.ID, 'Not Found')

    DATA_RESULT = (By.XPATH, '//p[@id="linkResponse"]//b')