from selenium.webdriver.common.by import By


class BrokenLinksLocators:
    VALID_IMAGE = (By.XPATH, '//div[@class="col-12 mt-4 col-md-6"]//div//img[@src="/images/Toolsqa.jpg"]')
    BROKEN_IMAGE = (By.XPATH, '//img[@src="/images/Toolsqa_1.jpg"]')
    VALID_LINK = (By.XPATH, "//a[text()='Click Here for Valid Link']")
    BROKEN_LINK = (By.XPATH, "//a[text()='Click Here for Broken Link']")