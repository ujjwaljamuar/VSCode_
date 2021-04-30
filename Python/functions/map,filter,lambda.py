#map
def square(num):
    return num**2
mynums=[1,2,3,4,5,6]
for item in map(square,mynums):
    print(item)
lists=list(map(square,mynums))
print(lists)

print('\n')

def splicer(mystring):
    if len(mystring)%2==0:
        return 'even'
    else:
        return mystring[0]
names=['ujjwal','nihu','chotu']
list1=list(map(splicer,names))
print(list1)

#filter - it filters the elements according tot the logic given
print('\n')

def check_even(num):
    return num%2==0
mynumss=[1,4,3,4,58,2,5]
list2=list(filter(check_even,mynumss))
print(list2)

#lambda-used instead of defining a function
print('\n')

list(map(lambda num:num**2,mynums))

print('\n')

list(filter(lambda num:num%2==0,mynumss))

print('\n')

m=list(map(lambda names:names[0],names))
print(m)

n=list(map(lambda names:names[::],names))
print(n)

o=list(map(lambda names:names[::-1],names))
print(o)