#def means definition

print('\nno.1\n')
def say_hello():
    print('hello')
    print('how')
    print('r')
    print('u')
say_hello()

print('\nno.2\n')
def say_hello(name):
    print(f'hello {name}')
say_hello('ujjwal')

print('\nno.3\n')
def say_hello(name='ujjwal'):
    print(f'hello {name}')
say_hello()

print('\nNo.4>\n')
def add_num(num1,num2):
    return num1+num2
def sub_num(num1,num2):
    return num1-num2
def prod_num(num1,num2):
    return(num1*num2)
def div_num(num1,num2):
    return num1/num2
print(add_num(10,20))
print(sub_num(20,30))
print(prod_num(-20,-40))
print(div_num(45,8))