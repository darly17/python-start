import newmod
x=8
#просмотр значений для работы
print(dir(newmod))
#расшифровка конкретного функционала модуля
print(help(newmod.newf))
#вызов функции из модуля
print(newmod.newf(3))


 #импорт всго функционала модуля или отдельных значений
from newmod import *


