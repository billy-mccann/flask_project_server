from dataclasses import dataclass
from random import randrange

@dataclass
class User:
    id: int
    name: str
    img_url: str

@dataclass
class RentalProperty:
    id: int
    nightly_price: int
    date_string: str

def create_random_user():
    return User(randrange(1_000_000), "Bill", "someCoolUrl")

def create_random_rental():
    return RentalProperty(randrange(1_000_000), randrange(1000), "someDate")