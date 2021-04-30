# to open a file use .open() method and to read the file and print the context use .read() method

myfile=open('myfile.txt')
print(myfile.read())

#it wont print twice bcz the cursorgoes to end of the file, so to print again use .seek(0)method to reset the cursor
myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(myfile.readlines())

#toopen any file any where in the system you have to provide location
newfile=open("E:\\newfile.txt")
print(newfile.read())

#always close the file after using it with .close() method
myfile.close()
newfile.close()

#if you don't want to close file nautnki use this to open a file
with open('myfile.txt') as my_new_file:
    contents=my_new_file.read()
    print(contents)

    #to read and write use mode="r" or 'w' or'r+' or 'a'
    #n use mode="w+"to overwrite and add text to the file

    with open('C:\\Users\\ujjwa\\Documents\\Python\\textfile.txt','w+') as f:
        f.write("three on three")
        f.seek(0)
        print(f.read())