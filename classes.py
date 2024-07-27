class Purse:
    def __init__(self,valuta,name='Unknown'):
        if valuta not in ('USD','EUR'):
             raise ValueError('Неверная валюта')
        self.__money=0.00
        self.valuta= valuta
        self.name= name

    
    def top_up_balance(self,howmany):
        self.__money=self.__money+howmany

    def top_down_balance(self,howmany):
        if self.__money-howmany < 0:
            print('Недостаточно средств')
            raise ValueError('Недостаточно средств')
        self.__money=self.__money-howmany
        return howmany

    def info(self) :
        print(self.__money) 

    def __del__(self):
        print('Кошелек удален')
     


x= Purse('USD','Ann')
y=Purse('USD','Vanya')
y.top_up_balance(100)
x.top_up_balance(y.top_down_balance(40))
x.info()
y.info()
