from selenium.webdriver.common.by import By


class FormsLocators:
    INPUT_FNAME = (By.ID, 'firstName')
    INPUT_LNAME = (By.ID, 'lastName')
    INPUT_EMAIL = (By.ID, 'userEmail')
    MALE_RADIOBUTTON = (By.ID, 'gender-radio-1')
    FEMALE_RADIOBUTTON = (By.ID, 'gender-radio-2')
    OTHER_RADIOBUTTON = (By.ID, 'gender-radio-3')
    INPUT_MOBILE = (By.ID, 'userNumber')
    INPUT_SUBJECTS = (By.ID, 'subjectsContainer')
    INPUT_DATE = (By.ID, 'dateOfBirthInput')
    SPORTS_CHECKBOX = (By.ID, 'hobbies-checkbox-1')
    READING_CHECKBOX = (By.ID, 'hobbies-checkbox-2')
    MUSIC_CHECKBOX = (By.ID, 'hobbies-checkbox-3')
    UPLOAD_BUTTON = (By.ID, 'uploadPicture')
    INPUT_ADDRESS = (By.ID, 'currentAddress')
    GENDER_RADIOBUTTONS_ALL = (By.XPATH, '//div[@class="custom-control custom-radio custom-control-inline"]')
    HOBBIES_RADIOBUTTONS_ALL = (By.XPATH, '//div[@class="custom-control custom-checkbox custom-control-inline"]')
    SUBMIT_BUTTON = (By.ID, 'submit')
    SUBMITING_FORM_WINDOW = (By.XPATH, '//div[@class="modal-content"]')
    RESULT_FORM = (By.XPATH, '//tr//td[2]')