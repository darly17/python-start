from datetime import datetime as dt
from time import sleep

class Player:

    __LVL,__HEALTHE=1,100
    __slots__=['__lvl','__health','__born']
    def __init__ (self):
        self.__lvl= Player.__LVL
        self.__health=Player.__HEALTHE
        self.__born=dt.now()
    def get_lvl(self):
        #геттер, для получения инкапсулированной информации
        return self.__lvl
    
    def set_lvl(self,numeric):
        self.__lvl+=numeric




x=Player()
print(x.set_lvl(10))
print(x.get_lvl())
        


