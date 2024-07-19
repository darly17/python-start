##менеджер контекста with as
##
##
##без менеджера
try:
    
    r=open('file.txt','a')
    r.write('something'+'\n')
    10/0
##если внутри кода записи/чтения файла возникает ошибка,
##то файл закрывается не корректно и информация теряется
    r.write('что-то')
finally:
 r.close()
 print('All working correcty')
    
# с менеджером

with open('file.txt','a') as r:
    r.write('something'+'\n')
    10/0
    r.write('что-то')
    
print('All working correcty')    

#открывает и закрывает файл автоматически
