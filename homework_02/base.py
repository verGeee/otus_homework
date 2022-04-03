from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel, CargoOverload
#from car import Car


class Vehicle(ABC):

    def __init__(self, weight = 1500, fuel = 100, fuel_consumption = 10):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError(self.fuel)

    def move(self, distance):
        fuel_consumption_calc = self.fuel_consumption * distance
        if self.fuel > fuel_consumption_calc:
            self.fuel = self.fuel - fuel_consumption_calc
        else:
            raise NotEnoughFuel(fuel_consumption_calc)

#new_vehicle = Vehicle(weight=1500, fuel=100, fuel_consumption=5)
#new_vehicle.start()
#new_vehicle.move(100)