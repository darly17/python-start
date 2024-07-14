import os
list_path=[]

for adress,papka,file in os.walk('C:\\'):
    for i in file:
        full_path = os.path.join(adress,i)
        list_path.append(full_path)


r = open('text.txt','w')
for j in list_path:
    r.write(j+'\n')
r.close()
