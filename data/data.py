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
    default_address: str = None

@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None

@dataclass
class Form:
    full_name: str = None
    email: str = None
    address: str = None
    default_address: str = None

@dataclass
class RandomFile:
    file: str = None