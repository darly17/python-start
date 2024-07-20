#декоратор-обработчик ошибок

def decor(f):
    
    #функция-обертка
    
    def wrapper():
        try:
            h=f()
        except :
            print('Повторите ввод')
            h=f()
        return h
    return wrapper

@decor # make=decor(make)
def make():
    enter=float(input('Enter number...'))
    return enter
@decor    
def make2():
    enter2=float(input('Enter second number...'))
    return enter2

make2()
make()



