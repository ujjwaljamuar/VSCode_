#try, except, finally

def add(n1,n2):
    print(n1+n2)
add(10,20)

number1=10
number2=input('please provide a number : ')
add(number1,number2)
print('something happened!') #this will not print because after an error it will stop executing ,so for that
try:
    #want to attempt this code may have an error
    result=10+10
except:
    print('it looks wrong!')
else:
    print('add went well')
    print(result)


