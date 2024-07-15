#обработка исключений

while True:
    try:
        enter = float(input('Введите число: '))
        print(100/enter)
        break

    except:
        print('Возникла ошибка')
        
      

#парсинг файлов
import sys

url = ['text1.txt', 'text2.txt', 'text.txt', 'text25.txt']

list_defect=[]
list_info = []

try:
    for i in url :
        try:
            r = open(i)
            list_info.append(r.read())
            print('without error')
        except :
            list_defect.append(r.read())
            print('error :( ')
            sys.exit()
            continue
    
finally:
    r=open('save.txt', 'a')
    for i in list_info:
        r.write(i)
    r.write (str(list_defect))
    r.close()
    print('Данные успешно сохранены')
    
