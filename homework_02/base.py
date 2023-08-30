from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False
    fuel = 40
    fuel_consumption = 6
    weight = 200

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started  == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError
        return self.started


    def move (self, distance):
        if distance * self.fuel_consumption <= self.fuel:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel



