#игра магазин
price={'cola':2.50,'fanta':2.30,'sprite':2.40,'shveps':3,'juce':2}

def buy():
    pay=0
    while True :
        enter = input('Что берем?\n')
        if enter=='end':
            break
        pay+=price[enter]
    return pay

print (buy(), ' рублей к оплате')
