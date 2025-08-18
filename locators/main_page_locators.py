from selenium.webdriver.common.by import By


class MainPageLocators:

    # # # Локаторы меню на главной странице # # #
    CARDS_MAIN_PAGE_CONTAINER = (By.XPATH, '//div[@class="category-cards"]')
    CARDS_ELEMENTS = (By.XPATH, '//h5[text()="Elements"]')