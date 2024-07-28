class Verification:


    def __init__ (self,login,password):
        self.login=login
        self.password=password
        self.__lenPassword()

    def __lenPassword (self):
        if len(self.password)<8:
            raise ValueError('week password')
        
    def save(self):
        with open ('users','a') as r:
            r.write(f'{self.login,self.password}'+ '\n')
            
# линеаризация
class A:
    def a(self):
        print('A')

class B:
    def a(self):
        print('B')

class C(B):
    def a(self):
        print('C')

class D(C,A):
    def a(self):
       #указать ОТ какого класса поиск а не в каком
       super(B,self).a()
       #для просмотра того, как наследуются функции в классах
       #или print(D.__mro__)
       print(self.__class__.__mro__)



D().a()

