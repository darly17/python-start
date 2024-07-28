from class2 import Verification
from tkinter import Tk,Button

class V2(Verification):
    def __init__(self,login,password,age):
       #питон сам ищет из какого родительского класса данная функция
       super().__init__(self,login,password)
       self.__save()
       self.age=age

    def show(self):
        return self.login, self.password
    
    def __save(self):
        with open ('users') as r:
         for i in r:
            if f'{self.login, self.password}'+'\n'== i:
               raise ValueError('такой уже есть')
        super().save(self)     
    
# class My_app(Tk):
   
#     def __init__(self):
#         Tk.__init__(self)
#         self.geometry('400x400')
#         self.setU()

#     def setU (self):
#         Button (self,text='Ok').pack()

# root = My_app()
# root.mainloop()

