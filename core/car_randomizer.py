from .enums import CarType, CarModel, CarEngineType, CarBrand
import random


class CarRandomizer:
    @staticmethod
    def get_random_type():
        return random.choice(tuple(CarType)).value

    @staticmethod
    def get_random_engine_type():
        return random.choice(tuple(CarEngineType)).value

    @staticmethod
    def get_random_brand():
        return random.choice(tuple(CarBrand)).value

    @staticmethod
    def get_random_color(cls):
        return random.choice(tuple(cls)).value

    @staticmethod
    def get_random_model(brand):
        if brand == CarBrand.AUDI.value:
            models = CarModel.AUDI.value

        elif brand == CarBrand.BMW.value:
            models = CarModel.BMW.value

        elif brand == CarBrand.MERCEDES.value:
            models = CarModel.MERCEDES.value

        elif brand == CarBrand.FORD.value:
            models = CarModel.FORD.value

        elif brand == CarBrand.MAZDA.value:
            models = CarModel.MAZDA.value

        elif brand == CarBrand.OPEL.value:
            models = CarModel.OPEL.value

        elif brand == CarBrand.SKODA.value:
            models = CarModel.SKODA.value

        elif brand == CarBrand.PEUGEOT.value:
            models = CarModel.PEUGEOT.value

        elif brand == CarBrand.TOYOTA.value:
            models = CarModel.TOYOTA.value

        elif brand == CarBrand.RENAULT.value:
            models = CarModel.RENAULT.value

        elif brand == CarBrand.VOLKSWAGEN.value:
            models = CarModel.VOLKSWAGEN.value

        elif brand == CarBrand.HYUNDAI.value:
            models = CarModel.HYUNDAI.value
        else:
            return None

        return random.choice(models)
