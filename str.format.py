#str.format()= optional method that gives users more control when displaying output

animal='cow'
item='moon'
#print('The'+ animal+'jumped over the'+item)

print('The {1:10} jumped over the {0}'.format(animal,item))
print('The {1:<10} jumped over the {0}'.format(animal,item))
print('The {1:>10} jumped over the {0}'.format(animal,item))
print('The {1:^10} jumped over the {0}'.format(animal,item))

number=3.14159

print('The number pi is {:.2f}'.format(number))

number1=100000

print('The number  {:,}'.format(number1))



number1=45

print('The number in bynary  {:b }'.format(number1))

