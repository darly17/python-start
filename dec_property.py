from datetime import datetime as dt
from time import sleep

class Player:

    __LVL,__HEALTHE=1,100
    __slots__=['__lvl','__health','__born']


    def __init__ (self):
        self.__lvl= Player.__LVL
        self.__health =Player.__HEALTHE
        self.__born=dt.now()


    @property
    def lvl(self):
        #геттер, для получения инкапсулированной информации
        return self.__lvl,f'{dt.now()-self.__born}'
    

    @lvl.setter
    def lvl(self,numeric):
        self.__lvl+=Player.__typeTest(numeric)
        if self.__lvl>=100:self.__lvl=100

    @classmethod
    def set_cls_field(cls,lvl=1,healthe=100):
        cls.__LVL=Player.__typeTest(lvl)
        cls.__HEALTHE=Player.__typeTest(healthe)

    @staticmethod 
    def __typeTest(value):
        if isinstance(value,int):
            return value
        else:
            raise TypeError('must be int')





x=Player()
x.lvl=2.9

print(x.lvl)


