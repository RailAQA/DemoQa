from selenium.webdriver.common.by import By


class MainPageLocators:

    # # # Локаторы меню на главной странице # # #
    CARDS_MAIN_PAGE_CONTAINER = (By.XPATH, '//div[@class="category-cards"]')
    CARDS_ELEMENTS = (By.XPATH, '//h5[text()="Elements"]')
    CARDS_FORMS = (By.XPATH, '//h5[text()="Forms"]')
    CARDS_ALERTS = (By.XPATH, '//h5[text()="Alerts, Frame & Windows"]')
    CARDS_WIDGETS = (By.XPATH, '//h5[text()="Widgets"]')
    CARDS_INTERACTIONS = (By.XPATH, '//h5[text()="Interactions"]')
    CARDS_BOOK = (By.XPATH, '//h5[text()="Book Store Application"]')