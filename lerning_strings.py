#learning_string

s = 'Let\'s write a string as "s"'
print(s)
               
a = "Lets write a stri\ng as 's'"
print(a)
               
b = 'Let\'s write a stri\nng as "s"'
print(b)
               

c = 'Let\'s write a string\ as "s"'
print(c)
               

url= r'https:\www.youtube.com\\new'
print(url)

s='stroka_texta'
print(s.upper())  #&lower
print(s.capitalize())
#методы не извеняют строку

path = 'C:/Users/PyHS/Desktop/s.py'
path1=path.replace('/','\\')
print(path1)
r = path1.split('\\')
print(r[-1])




f = open('text.txt')
r1=f.read()
list_zn=['(',')','"','\n']
for i in list_zn:
    r1=r1.replace(i,'')
print(r1)


r2=r1.split()

new_text='_*_'.join(r2)
print(new_text)


  
