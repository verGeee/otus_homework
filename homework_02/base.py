from abc import ABC
import homework_02

class Vehicle(ABC):

    def __init__(self, weight = 1500, fuel = 100, fuel_consumption = 10):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if (self.started == False and self.fuel > 0) or self.fuel > 0:
            self.started = True
        else:
            raise homework_02.exceptions.LowFuelError

    def move(self, distance):
        fuel_consumption_calc = self.fuel_consumption * distance
        if self.fuel >= fuel_consumption_calc:
            self.fuel = self.fuel - fuel_consumption_calc
        else:
            raise homework_02.exceptions.NotEnoughFuel