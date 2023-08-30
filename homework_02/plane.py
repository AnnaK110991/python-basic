"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


#from homework_02.engine import Engine

class Plane(Vehicle):
    cargo = 0
    max_cargo  = None

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
         super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
         self.max_cargo  = max_cargo

    def load_cargo (self, num):
        if num + self.cargo <= self.max_cargo:
            self.cargo = num + self.cargo
        else:
            raise CargoOverload


    def remove_all_cargo (self):
        cargo_befor_null  = self.cargo
        self.cargo = 0
        return cargo_befor_null


