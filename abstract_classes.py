#Prevent a user from creating an object of that class
#+compels a user to override abstract methods in a child class

#abstract class = a class which contains one or more abstract methods.
#abstract method=a method that has a declaration but doesn't have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        print('jfisjf')
    @abstractmethod
    def stop(self):
        print('stop')


class Car (Vehicle):
    def go(self):
        print('car')
    def stop(self):
        print('stop')


class Motorcycle (Vehicle):
    def go(self):
        print('motorcycle')

    def stop(self):
        print('stop')

    

car=Car()
motorcycle=Motorcycle()
car.go()
car.stop()





