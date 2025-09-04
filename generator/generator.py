import random
import os
from locators.check_box_locators import CheckBoxLocators
from locators.buttons_locators import ButtonsLocators
from locators.links_locators import LinksPageLocators
from data.data import Person, Date, Form, RandomFile
from faker import Faker
locators = CheckBoxLocators()
button_locators = ButtonsLocators()
link_locators = LinksPageLocators()

faker_en = Faker('En')
faker_ru = Faker('Ru')
Faker.seed()

def generated_person():
    yield Person(first_name=faker_en.first_name(), 
                 last_name=faker_en.last_name(), 
                 email=faker_en.ascii_free_email(), 
                 phone=random.randrange(7111111111, 7999999999), 
                 subjects=faker_en.text(), 
                 address=faker_en.street_address(),
                 gender=random.randrange(2),
                 hobbies=random.randrange(2),
                 default_address=faker_ru.street_name()
                 )

def generated_date():
    yield Date(day=faker_en.day_of_month(), 
               month=faker_en.month_name(), 
               year=faker_en.year())
    
def generated_subjects():
    subjects = ["Maths", "Chemisty", "Computer Science", "Commerce", "Economics"]
    return random.choice(subjects)

def generated_form():
    yield Form(full_name=faker_ru.first_name(), 
               email=faker_ru.ascii_free_email(), 
               address=faker_en.street_address(), 
               default_address=faker_ru.street_name())
    
def generated_check_box():
    check_box = [locators.DESKTOP_CHECKBOX, locators.DOCUMENTS_CHECKBOX, locators.DOWNLOADS_CHECKBOX]
    return random.choice(check_box)

def generated_radio_button():
    return random.randrange(0, 2)

def generated_button():
    return random.randrange(2)

def generated_links():
    choice = [link_locators.BAD_REQUEST_LINK, link_locators.CREATED_LINK, link_locators.FORBIDDEN_LINK, link_locators.MOVED_LINK, link_locators.NO_CREATED_LINK, link_locators.NOT_FOUND_LINK, link_locators.UNAUTH_LINK]
    return random.choice(choice)

def generated_links_result():
    choice = [link_locators.DATA_RESULT[0], link_locators.DATA_RESULT[1]]
    return random.choice(choice)

def generated_file():
    random_file = "/Users/ann/Downloads/" + faker_ru.name()
    return random_file

def generated_new_file():
    file = faker_ru.name_male()
    path = f"/Users/ann/Downloads/{file}.txt"
    with open(path, 'w') as new_file:
        new_file.write('Hello World?')
    return path, file

def generated_alert_acept():
    return random.randrange(0,2)