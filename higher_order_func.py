# #   higher Order function= a funcktion that either:
# #   1. accepts a function as an argument
# #  or
# #  2. returns a function


# #for number 1

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text=func("Hello")
    print(text)


hello(loud)


#2
#делитель
def divisor(x):
    def dividend(y):
        return y/x
    return dividend


divide=divisor(2)
print(divide(6))