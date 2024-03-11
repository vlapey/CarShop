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


class CarEngineType(Enum):
    DIESEL = 'diesel'
    GASOLINE = 'gasoline'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class CarBrand(Enum):
    AUDI = 'audi'
    MERCEDES = 'mercedes'
    BMW = 'bmw'
    FORD = 'ford'
    MAZDA = 'mazda'
    OPEL = 'opel'
    SKODA = 'skoda'
    PEUGEOT = 'peugeot'
    TOYOTA = 'toyota'
    RENAULT = 'renault'
    VOLKSWAGEN = 'volkswagen'
    HYUNDAI = 'hyundai'


class CarModel(Enum):
    AUDI = ('Q5', 'Q7', 'A3')
    MERCEDES = ('GLA', 'EQS', 'GLS')
    BMW = ('3 series', '5 series', '7 series')
    FORD = ('Focus', 'Transit', 'Kuga')
    MAZDA = ('MX30', 'CX30', 'CX4')
    OPEL = ('Mokka', 'Vivaro', 'Astra')
    SKODA = ('Kodiaq', 'Kamiq', 'Octavia')
    PEUGEOT = ('3008', '5008', 'Rifter')
    TOYOTA = ('Camry', 'RAV4', 'Hilux')
    RENAULT = ('Koleos', 'Megane', 'Laguna')
    VOLKSWAGEN = ('Golf', 'Polo', 'Tiguan')
    HYUNDAI = ('Palisade', 'Venue', 'Elantra')


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
