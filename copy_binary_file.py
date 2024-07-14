import os
r= open('e.exe','rb')
y= open ('Copy_e.exe','wb')

while True:
    var=r.read(1024*1024)
    print(var.__sizeof__())#сколько ОП занимает
    if var.__sizeof__()==33:
        break
    
    y.write(var)

r.close()
y.close()
    
