#выражения генератор

#ordinary generator
h=['https:\\www.site.com','https:\\www.randomsite','https:\\www.randomsite0',
   'https:\\www.randomsite1','https:\\www.randomsite2','https:\\www.randomsite3']
n=[x.split('\\')[1] for x in h if '.com' in x]

# generator expression
z=(x.split('\\')[1] for x in h )




import os

n=[i for i in os.walk('C:\\')]#list generator
z=(i for i  in os.walk('C:\\'))#generator expression

