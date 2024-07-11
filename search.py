import os
import time
spisok =[]

for adress, dirs, files in os.walk('C:\\Users\User\Desktop\for_example'):
    for file in files:
        full = os.path.join (adress, file)
        if time.time()-os.path.getctime(full) < 86400:
            spisok.append (full)

print(spisok)

#проверка на создание файла в течение суток
    
