#multiple inheritance = when a child class is derived from more than one parent class

# class Prey:
#     def flee(self):
#         print ("This animal flees")

# class Predator:
#     def hunt(self):
#         print("This animal is hunting")


# class Rabbit(Prey):
#     pass

# class Hawk (Predator):
#     pass

# class Fish(Prey,Predator):
#     pass

# fish=Fish()
# fish.flee()
# fish.hunt()


# method chaining =calling multiple methods sequentially each call performs an action on the same object and returns self


class Car:

    def turn_on(self):
        print("start the engine")
        return self

    def drive(self):
        print("drive")
        return self
    
    def brake(self):
        print("step on the brakes")
        return self

    def turn_off(self):
        print("turn off the engine")
        return self









