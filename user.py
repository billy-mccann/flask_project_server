from dataclasses import dataclass
from random import randrange

@dataclass
class User:
    id: int
    name: str
    img_url: str

@dataclass
class CellContent:
    id: int
    title: str
    left: str
    right: str

@dataclass
class RentalProperty:
    id: int
    nightly_price: int
    date_string: str
    img_url: str

def create_random_user():
    return User(randrange(1_000_000), "Bill", "someCoolUrl")

def create_random_cell(num):
    return CellContent(num, str(num) , "lefty", "righty")

def create_random_rental():
    rand_num = randrange(100) + 200
    img_url = "https://picsum.photos/id/"+str(rand_num)+"/100"
    return RentalProperty(randrange(1_000_000), rand_num , "someDate", img_url)

