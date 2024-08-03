# class Car:
#     color=None

# class Moto:
#     color=None

# def change_color(car,color):
#     car.color=color



# car1=Car()
# car2=Car()
# car3=Car()
# bike=Moto()

# change_color(car1,'red')
# change_color(car2,'white')
# change_color(car3,'black')
# change_color(bike,'blue')

# print(car1.color)
# print(car2.color)
# print(car3.color)
# print(bike.color)




#Duck typing= concept where the class of an object is less important than the methods/attributes that the classs might have
#class type is not checked if minimum methods/attributes are present 


class Duck():
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print('Quacking')


class Chicken():
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print('Clucking')


class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print('You caught the critter')


duck=Duck()
chicken=Chicken()
person=Person()

person.catch(duck)



