""""""


from prac_08.car import Car
from random import randint

class Unreliable_Car(Car):
    """"""

    def __init__(self, name, fuel, reliability = 0):
        """"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """"""
        distance_driven = 0
        if randint (0, 100) > self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven