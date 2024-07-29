# #file detection
# import os

# path='C:\\Users\\User\\Desktop\\text.txt'

# if os.path.exists(path):
#     print('Exists')
#     if os.path.isfile(path):
#         print("It's a file")
#     elif os.path.isdir(path):
#         print("It's a dir")
# else:
#     print("Doesn't Exists")




#copy files
# copyfile()=copies contents of a file # 2 args src, dst
#copy()=copifile()+permission mode+ destination can be a directory
# copy2()=copy()+ copies metadata(file's creation and modificatoion times) import shutil


#move file
# import os
# source='test.txt'
# destination='C:\\Users\\User\\Desktop\\text.txt'
# try:
#     if os.path.exists(destination):
#         print('there is already a file there')
#     else:
#         os.replace(source,destination)
#         print(source + 'was moved')
# except FileNotFoundError:
#     print (source+'was not found')


#delete file
import os
import shutil
path ='test.txt'


try:
    os.remove(path)#DELETE a file
    #os.rmdir(path) #delete a file or empty directory
    #shutil.rmtree(path)#delete filesand or folders

except FileNotFoundError:
    print("That file wasn't found")








