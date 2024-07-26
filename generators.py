
#генераторы списков, словарей и множеств
h=[1,2,3,3,4,5,6,7,87,6,7]
newh=[x*2 for x in h]
f={x: x*3 for x in h}


# generator with loop and a condition
g=[x for x in h if not x%2]

  
###nested loop
import os

h=[1,2,3,3,4,5,6,7,87,6,7]

g=[os.path.join (a,i) for a,b,c in os.walk('C:\\') for i in c if '.txt' in i]




price={'cola':2.50,'fanta':2.30,'sprite':2.40,'shveps':3,'juce':2}

new_d={i:round(price[i]*0.85,2) for i in price.keys()}
