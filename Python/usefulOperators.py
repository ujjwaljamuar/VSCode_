#range 
for num in range(0,10):
    print(num)


for num in range(0,10,2):
    print(num)

print(list(range(0,11,2)))

index_count=0
for letters in 'abcdef':
    print('at index {} the letter is {}'.format(index_count,letters))
    index_count+=1

#another way with enumerate word
word='ujjwal'
for item,letter in enumerate(word):
    print(item)
    print(letter)
    print('\n')

#another way
mylist1=[1,2,3,4,5,6]
mylist2=['a','b','c']
mylist3=[100,200,300]
print(zip(mylist1,mylist2,mylist3))

#another way
for item in zip(mylist1,mylist2,mylist3):
    print(item)
    print(list(zip(mylist1,mylist2,mylist3)))

#in operator
print('x' in [1,2,3])

d={'mykey':152}
print(152 in d.values())

#min and max , shuffle
lists=[1,25,4,3,9,7,0]
print(min(lists))
print(max(lists))
from random import randint

print(randint(0,100))

mynum=randint(0,50)
print(mynum)

input('enter a number :-')
