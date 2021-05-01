#while loops

x=0
while x<9:
    print(f"the value of x is {x}")
    x+=1
else:
    print('the number is less than 9')
#break, continue, pass keywords

y=[1,2,3]
for item in y:
    pass # does nothing except it won't get you error (avoid syntax errors)

z=[1,2,3]
for item in z:
    pass
print('end of the script')

#continue
mystring='sammy'
for letter in mystring:
    if letter=='a':
        continue
    print(letter)

#break
mystring='sammy'
for letter in mystring:
    if letter=='a':
        break
    print(letter)

#while loops

t=0
while t<5:
    if t==4:
        break
    print(t)
    t+=1