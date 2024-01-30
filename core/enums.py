from enum import Enum


class CarType(Enum):
    sedan = "Sedan"
    coupe = "Coupe"
    hatchback = "Hatchback"
    minivan = "Minivan"
    electric = "Electric"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Color(Enum):
    red = "Red"
    blue = "Blue"
    yellow = "Yellow"
    green = "Green"
    black = "Black"
    white = "White"
    cyan = "Cyan"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class IsHavingLicense(Enum):
    y = "yes"
    n = "no"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Role(Enum):
    CUSTOMER = 'customer'
    VENDOR = 'vendor'
    DEALER = 'dealer'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    def __str__(self):
        return self.value
