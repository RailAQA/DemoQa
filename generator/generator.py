import random

from data.data import Person, Date
from faker import Faker

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
                 hobbies=random.randrange(2)
                 )

def generated_date():
    yield Date(day=faker_en.day_of_month(), 
               month=faker_en.month_name(), 
               year=faker_en.year())
    
def generated_subjects():
    subjects = ["Maths", "Chemisty", "Computer Science", "Commerce", "Economics"]
    return random.choice(subjects)