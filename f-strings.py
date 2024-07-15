#форматирование строк

enter = input('Your name: ')

s='Hello %s, I am %s'%(enter,'Python')

f='Hello {}, I am {}'.format(enter,'Python')
print(f)


f1='Hello {1}, I am {0}'.format(enter,'Python')
print(f1)

f_string=f'Hello {enter}, I can do some things in f-string, for example the length of your name is {len(enter)}'
print(f_string)
