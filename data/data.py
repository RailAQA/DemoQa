from dataclasses import dataclass

@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: int = None
    subjects: str = None
    address: str = None
    gender: int = None
    hobbies: int = None

@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None