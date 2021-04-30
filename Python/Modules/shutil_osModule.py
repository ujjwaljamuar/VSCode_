f=open('practice.txt','w+')
f.write('this is a test string')
f.close()

import os
print(os.getcwd())     #print the directory
print(os.listdir())    #list all the working directories
print(os.listdir('C:\\Users')) 

import shutil   # use to move files
shutil.move('practice.txt','C:\\Users\\ujjwa\\Documents')

print('\n')
# for deleting files: 

import send2trash
send2trash.send2trash('practice.txt')

