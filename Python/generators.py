def create_cubes(n):
    result=[]
    for x in range(n):
        result.append(x**3)
    return print(result)
create_cubes(10)

# other way as a generator 
def cubes(n):
    for x in range(n):
        yield x**3
for x in cubes(10):
    print(x)

#or
print(list(cubes(10)))

print('\n')

def gen_fibo(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b
for num in gen_fibo(10):
    print(num)

print('\n')

def simple_gen():
    for x in range(3):
        yield x

for num in simple_gen():
    print(num)

print('\n')

g=simple_gen()
print(next(g))
print(next(g))
print(next(g))

print('\n')

s='hello'
for letter in s:          
    print(letter)                #next keyword won't work here so,

# iter() function
print('\n')
s_iter=iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))