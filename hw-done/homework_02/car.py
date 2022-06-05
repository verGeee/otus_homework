"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base


class Car(base.Vehicle):
    def __init__(self, weight=1500, fuel=100, fuel_consumption=10):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, class_engine: object):
        self.engine = class_engine