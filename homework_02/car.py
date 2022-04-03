"""
создайте класс `Car`, наследник `Vehicle`
"""

from base import Vehicle

class Car(Vehicle):
    pass


new_car = Car(weight=1500, fuel=100, fuel_consumption=10)
print(vars(new_car))