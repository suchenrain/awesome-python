# coding=utf-8
#  inheritance:behaviors and characteristics
# 继承：行为和特征
# python 2.7.15


class Car:
    def __init__(self, wheels, seats, velocity):
        self.wheels = wheels
        self.seats = seats
        self.velocity = velocity


myCar = Car(2, 5, 210)

print myCar.wheels
print myCar.seats
print myCar.velocity


class ElectricCar(Car):
    def __init__(self, wheels, seats, v):
        Car.__init__(self, wheels, seats, v)


myElecCar = ElectricCar(3, 7, 300)

print myElecCar.seats
print myElecCar.velocity
print myElecCar.wheels
