
def cool():
    
    def super_cool():
        print('i am very cool')
    return super_cool()
some_func=cool()
some_func
    


def hello():
    print( 'hi ujj')

def other(some_def_func):
    print('other code runs here')
    print(some_def_func())

hello()
other(hello)

print('\n')

def new_decorator(original_func):
    def wrap_func():
        print('some extra code before the original func')
        original_func()
        print("some extra code after it")
    return wrap_func()

def func_needs_Dec():
    print('i want to be decorated!!')

decorated_func=new_decorator(func_needs_Dec)
decorated_func

print('\n')

@new_decorator
def func_needs_Dec():
    print('i want to be decorated!!')

func_needs_Dec