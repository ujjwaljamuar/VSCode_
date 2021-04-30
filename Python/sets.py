# sets are unordered collection of unique elements.(only one representative of same object) use curly braces{} or lower braces()

myset=set()
myset.add(1)
myset.add(2)
myset.add(2)
myset.add(1)
print(myset)   #it prints only unique values

mylist=[1,2,2,2,1,4,4,4,6,7,7,3,1]
set(mylist)
print(set(mylist))  #only unique values are printed

