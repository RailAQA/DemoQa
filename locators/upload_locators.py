from selenium.webdriver.common.by import By


class UploadPageLocators:
    DOWNLOAD_BUTTON = (By.ID, 'downloadButton')
    SELECT_FILE_BUTTON = (By.ID, 'uploadFile')
    FAKE_PATH = (By.ID, 'uploadedFilePath')