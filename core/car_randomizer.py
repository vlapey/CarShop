from src.car.models import Car
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
    def randomize_car():
        mileage = random.randint(0, 10000)
        price = random.randint(2000, 100000)
        horsepower = random.randint(150, 500)
        torque = random.randint(100, 400)
        brand = CarRandomizer.get_random_brand()

        car = Car(
            brand=brand,
            model=CarRandomizer.get_random_model(brand),
            engine=CarRandomizer.get_random_engine_type(),
            horsepower=horsepower,
            torque=torque,
            car_type=CarRandomizer.get_random_type(),
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


class SpecsRandomizer:
    @staticmethod
    def get_random_engine_type():
        return CarRandomizer.get_random_engine_type()

    @staticmethod
    def get_random_horsepower():
        min_horsepower = Car.objects.order_by('horsepower').values().first()['horsepower']
        max_horsepower = Car.objects.order_by('-horsepower').values().first()['horsepower']
        return random.randint(min_horsepower, max_horsepower)

    @staticmethod
    def get_random_mileage():
        min_mileage = Car.objects.order_by('mileage').values().first()['mileage']
        max_mileage = Car.objects.order_by('-mileage').values().first()['mileage']
        return random.randint(min_mileage, max_mileage)

    @staticmethod
    def get_random_price():
        min_price = Car.objects.order_by('price').values().first()['price']
        max_price = Car.objects.order_by('-price').values().first()['price']
        return random.randint(min_price, max_price)

    @staticmethod
    def randomize_specs():
        car = Car(
            engine=CarRandomizer.get_random_engine_type(),
            horsepower=SpecsRandomizer.get_random_horsepower(),
            car_type=CarRandomizer.get_random_type(),
            mileage=SpecsRandomizer.get_random_mileage(),
            price=SpecsRandomizer.get_random_price()
        )
        return car
