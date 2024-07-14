import math
PI = math.pi

def rad():
    n = float(input('Введите диаметр'))
    return n/2
def he():
    m  = float(input('Введите высоту'))
    return m

def volume():
    r = rad()
    h = he()
    s = PI*r**2
    v = s*h
    return v

print (volume())
