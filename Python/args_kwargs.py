def myfunc(a,b):
    #returns 5% of the total sum
    return sum((a,b)) *0.05
result=myfunc(40,60)
print(result)

#2
print('\n')
def myfunc(s,t,u=0,y=0,z=0):
    #returns 5% of the total sum
    return sum((s,t,u,y,z)) *0.05
result=myfunc(40,60,80)
print(result)

#use of *args (its a choice you can chose any keyword with *)
print('\n')
def myfun(*args):
    print(args)
myfun(1,2,3,4,5)

def myfun(*args):
    for items in args:
        print(items)
myfun(1,2,3,4,5)


#4
print('\n')
def myfun(*spam) :
    return sum(spam) *0.05
myfun(1,2,3,4,5,6,9,8,7,4,5,455,55)

print('\n')

#**kwargs
def mfun(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}.'.format(kwargs['fruit']))
    else:
        print('i didnt find anything here.')
mfun(fruit='banana',veggie='paneer')
print('\n')

#*args and **kwargs at same time
def both(*args,**kwargs):
    print('i would like to have {} {} and a {}.'.format(args[0],kwargs['food'],kwargs['fruit']))
both(4,6,8,fruit='banana',food='eggs')