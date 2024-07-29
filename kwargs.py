 #**kwards=parametr that will pack all rguments into a dictionary
# useful  so that a function can accept a varying amount of keyword args


def hello(**kwargs):
    print('Hello'+" "+ kwards['first']+" "+kwards['middle']+" "+kwards['last'])
    print('hello',end=" ")
    for key,value in kwargs.items():
        print(value,end='')


hello(first='Bro',middle='Kevin',last='Code')


