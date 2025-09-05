from pages.base_page import BasePage
from generator.generator import generated_person
from locators.elements.forms_locators import FormsLocators
form_locators = FormsLocators()


class FormsPage(BasePage):
    
    
    def zapolnenie_formi(self):
        person = next(generated_person())
        first_name = person.first_name
        last_name = person.last_name
        phone = person.phone
        email = person.email
        hobbies = person.hobbies
        #subjects = person.subjects
        address = person.address
        gender = person.gender
        self.scroll_to(element=self.find(form_locators.INPUT_FNAME))
        self.find(form_locators.INPUT_FNAME).send_keys(first_name)
        print(f'Ввел в поле "first_name" значение {first_name}')
        self.scroll_to(element=self.find(form_locators.INPUT_LNAME))
        self.find(form_locators.INPUT_LNAME).send_keys(last_name)
        print(f'Ввел в поле "last_name" значение {last_name}')
        self.scroll_to(element=self.find(form_locators.INPUT_MOBILE))
        self.find(form_locators.INPUT_MOBILE).send_keys(phone)
        print(f'Ввел в поле "phone" значение {phone}')
        self.scroll_to(element=self.find(form_locators.GENDER_RADIOBUTTONS_ALL))
        self.finds(form_locators.GENDER_RADIOBUTTONS_ALL)[gender].click()
        print(f'В gender выбрал значение {gender + 1}')
        self.scroll_to(element=self.find(form_locators.INPUT_EMAIL))
        self.find(form_locators.INPUT_EMAIL).send_keys(email)
        print(f'Ввел в поле "email" значение {email}')
        self.scroll_to(element=self.find(form_locators.HOBBIES_RADIOBUTTONS_ALL))
        self.finds(form_locators.HOBBIES_RADIOBUTTONS_ALL)[hobbies].click()
        print(f'Ввел в поле "hobbies" значение {hobbies + 1}')
        self.scroll_to(element=self.find(form_locators.INPUT_ADDRESS))
        self.find(form_locators.INPUT_ADDRESS).send_keys(address)
        print(f'Ввел в поле "address" значение {address}')
        self.scroll_to(element=self.find(form_locators.SUBMIT_BUTTON))
        self.find(form_locators.SUBMIT_BUTTON).click()
        self.element_is_visible(15, form_locators.SUBMITING_FORM_WINDOW)
        return [first_name, last_name, email, str(phone), address, gender]


    def data_in_opened_window_form(self):
        return [i.text for i in self.finds(form_locators.RESULT_FORM)]