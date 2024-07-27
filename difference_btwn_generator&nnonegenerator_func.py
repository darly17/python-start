
## без ф-ции генератора
def some():
    list_txt=[]
    with open('file.txt') as f:
        for x in f:
            list_txt.append(x)
    return list_txt



# c ф-цией генератором
def some():
    with open('file.txt') as f:
        for x in f:
            yield x

for i in some():
    print(i.split())
