#walrus== морж
#walrus operator:=
#aka assignment expression
#assigns values to variables as part of a larger expression
#присваивает значения переменным как части большего выражения


print(happy:=True)


foods=list()

while True:
    food=input('What would you like?')
    if food =='quit':
        break
    foods.append(food)


#or

while food:=input('What would you like?')!='quit':
    foods.append(food)


