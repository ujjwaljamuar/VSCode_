#tuples are a type of list but they are immutable(cant be changed)

t=('a','a','b')
mylist=[4,5,6]
print(type(t))
print(type(mylist))
#to count how many times an object occur in tuple use .count() method

print(t.count('a'))

#to print at what index postion object is use .index() method
print(t.index("a"))
 