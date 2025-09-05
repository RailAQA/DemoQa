from selenium.webdriver.common.by import By



class CheckBoxLocators:
    HOME_TOGGLE_BUTTON = (By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]')
    HOME_CHECKBOX = (By.XPATH, '//label[@for="tree-node-home"]')
    DESKTOP_TOGGLE_BUTTON = (By.XPATH, '//li[@class="rct-node rct-node-parent rct-node-collapsed"][1]//span[@class="rct-text"]//button[@type="button"]')
    DESKTOP_CHECKBOX = (By.XPATH, '//label[@for="tree-node-desktop"]')
    DOCUMENTS_TOGGLE_BUTTON = (By.XPATH, '//li[@class="rct-node rct-node-parent rct-node-collapsed"][2]//span[@class="rct-text"]//button[@type="button"]')
    DOCUMENTS_CHECKBOX = (By.XPATH, '//label[@for="tree-node-desktop"]')
    DOWNLOADS_TOGGLE_BUTTON = (By.XPATH, '//li[@class="rct-node rct-node-parent rct-node-collapsed"][3]//span[@class="rct-text"]//button[@type="button"]')
    DOWNLOADS_CHECKBOX = (By.XPATH, '//label[@for="tree-node-downloads"]')
    ALL_CHECK_BOX_SUBPARENT = (By.XPATH, '//li[@class="rct-node rct-node-parent rct-node-collapsed"]')
    ALL_TOGGLES_SUBPARENT = (By.XPATH, '//li[@class="rct-node rct-node-parent rct-node-collapsed"]//span[@class="rct-text"]//button')
    TEXT_RESULTS = (By.XPATH, '//span[@class="text-success"]')