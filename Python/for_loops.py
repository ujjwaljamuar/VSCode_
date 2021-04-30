#for loops

my_iterable=[1,2,3,4,5,6,7,8,9,10]

#type1
for jelly in my_iterable:
    print(jelly)
#type2
for number in my_iterable:
    print('ujjwal')
# type3
for num in my_iterable:
    if num%2==0:
        print(num)
    else:
        print(f'odd number : {num}')

#type 4
for num in my_iterable:
    if num%2==0:
        print(num)

#type5
list_sum=0
for bro in my_iterable:
    list_sum=list_sum + bro

print(list_sum)

#type6
my_String="hello world"
for letters in my_String:
    print(letters)

#type7
for letters in "hello world":
 print(letters)

 #type8
 tup=(1,2,3)
 for items in tup:
    print(len(tup))
    

 mylist=[(1,2),(4,5),(6,7),(7,9)]
 for (a,b) in mylist:
  print(a)
#type new
d={'k1':1,'k2':2,'k3':3}
for a,b in d.items():
    print(b)
  
