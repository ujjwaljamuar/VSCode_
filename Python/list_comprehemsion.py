mystring='hello'
mylist=[]
for letter in mystring:
    mylist.append(letter)
    print(mylist)
print(mylist)
    
mylist1 = [x for x in range(0,11)]
print(mylist1)

mylist2=[num**2 for num in range(0,16)]
print(mylist2)

mylist3=[x for x in range(0,11) if x%2==0]
print(mylist3)

celcius=[0,10,22,37.8]
fahrenheit=[((9/5)*temp +32) for temp in celcius]
print(fahrenheit)

fahrenheit=[]
for temp in celcius:
    fahrenheit.append(((9/5)*temp +32))
print(fahrenheit)

output=[x if x%2==0 else 'is odd here' for x in range(0,11)]
print(output)