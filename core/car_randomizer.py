from src.car.models import Car, CarSpecification
from .enums import CarType, CarModel, CarEngineType, CarBrand, Color
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
    def get_random_color():
        return random.choice(tuple(Color)).value

    @staticmethod
    def randomize_car_specification():
        horsepower = random.randint(150, 500)
        torque = random.randint(100, 400)
        brand = CarRandomizer.get_random_brand()
        car_specification = CarSpecification(
            brand=brand,
            model=CarRandomizer.get_random_model(brand),
            engine=CarRandomizer.get_random_engine_type(),
            horsepower=horsepower,
            torque=torque,
            car_type=CarRandomizer.get_random_type()
        )

        car_specification.save()

        return car_specification

    @staticmethod
    def randomize_car():
        mileage = random.randint(0, 10000)
        price = random.randint(2000, 100000)

        car_specification = CarRandomizer.randomize_car_specification()
        car = Car(
            specification=car_specification,
            color=CarRandomizer.get_random_color(),
            mileage=mileage,
            price=price
        )

        return car

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
