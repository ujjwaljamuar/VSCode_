#lists are same as arrays in java
#lists are mutable it means they can change.

my_list=["ujjwal",2,23.2]
another_list=["jamuar",45,12.2]
new_list=my_list+another_list
print(my_list)
print(len(my_list))     # it prints length of the list.

print(my_list[0]) #indexing

print(my_list[1:]) #slicing

#concatenate
print(my_list+another_list) #or
print(new_list)

#changing objects in lists
my_list[0]='Nivedita'
print(my_list)

#add new object to the list ny using .append()
my_list.append('birendra')
print(my_list)

#remove objects from a list by .pop() method
my_list.pop()
print(my_list)

my_list.pop(0)
print(my_list)

#sort objects ny .sort() method
letters_list=['x','e','a','g','c']
print(letters_list)
num_list=[4,7,3,2,0,1,5]

letters_list.sort()
print(letters_list)

print(num_list)
num_list.sort()
print(num_list)

#sort list in descending order using .reverse() method
num_list.reverse()
print(num_list)