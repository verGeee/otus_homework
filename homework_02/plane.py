"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02 import base
from homework_02 import exceptions

class Plane(Vehicle):

    def __init__(self, weight = 1500, fuel = 100, fuel_consumption = 10, max_cargo = 100):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo



    def load_cargo(self, current_cargo):
        if self.cargo + current_cargo < self.max_cargo:
            self.cargo = self.cargo + current_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo