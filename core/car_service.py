from src.car.models import Car
from src.dealer.models import Dealer
from src.loyalties.models import VendorsLoyalties, DealersLoyalties
from .enums import CarType, CarModel, CarEngineType, CarBrand, Color
import random
from django.utils import timezone


class CarFinder:
    @staticmethod
    def get_cars_by_filters(wanted_car_specs, wanted_car_types):
        cars = Car.objects.filter(vendor__isnull=False)
        if not cars:
            return cars

        cars = cars.filter(engine=wanted_car_specs.engine)

        after_filter_cars = cars.filter(horsepower__lte=wanted_car_specs.horsepower)
        if not after_filter_cars:
            cars = cars.filter(horsepower__gte=wanted_car_specs.horsepower)
        else:
            cars = after_filter_cars
        del after_filter_cars

        counter = 0
        while not cars or counter < 2:
            cars = cars.filter(car_type__in=wanted_car_types)
            counter += 1

        after_filter_cars = cars.filter(mileage__lte=wanted_car_specs.mileage)
        if not after_filter_cars:
            cars = cars.filter(mileage__gte=wanted_car_specs.mileage)
        else:
            cars = after_filter_cars
        del after_filter_cars

        after_filter_cars = cars.filter(price__lte=wanted_car_specs.price).order_by('price')
        if not after_filter_cars:
            cars = cars.filter(price__gte=wanted_car_specs.price).order_by('price')
        else:
            cars = after_filter_cars
        del after_filter_cars

        return cars

    @staticmethod
    def find_cheapest_car_and_discount(dealer_or_customer):
        selector = True
        if isinstance(dealer_or_customer, Dealer):
            selector = False

        wanted_car_specs = SpecsRandomizer.randomize_specs()
        wanted_car_types = SpecsRandomizer.get_random_type()
        cars = CarFinder.get_cars_by_filters(wanted_car_specs, wanted_car_types)
        if not cars:
            print("No cars found with such filters")
            return

        discount = CarFinder.get_active_discount(cars, selector)
        discounted_prices = []
        for car in cars:
            discounted_price = car.price - car.price * (discount / 100)
            discounted_prices.append(discounted_price)
        cheapest_index = discounted_prices.index(min(discounted_prices))
        cheapest_car = cars[cheapest_index]
        return [cheapest_car, discount]

    @staticmethod
    def get_active_discount(cars, selector):
        today = timezone.now()
        if selector:
            has_discount = DealersLoyalties.objects.filter(
                car__in=cars,
                dealer__in=[car.dealer for car in cars],
                end_date__gte=today
            )
        else:
            has_discount = VendorsLoyalties.objects.filter(
                car__in=cars,
                vendor__in=[car.vendor for car in cars],
                end_date__gte=today
            )

        if not has_discount:
            return 0

        loyal = has_discount.order_by('-discount').first()
        return loyal.discount


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
    def get_random_type():
        car_type_list = []
        while len(car_type_list) < 3:
            car_type_list.append(CarRandomizer.get_random_type())
            car_type_list = list(dict.fromkeys(car_type_list))
        return car_type_list

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
