def func1(n):
    return print([str(num) for num in range(n)])
func1(10)

def func2(n):
    return print(list(map(str,range(n))))
func2(10)

import time
# current time before run
start_time=time.time()
# run code
res1=func1(1000)
# current time after run
end_time=time.time()
# elapsed time
elapsed_time=end_time-start_time

print(elapsed_time)

print('\n')
#for func2

# current time before run
start_time=time.time()
# run code
res1=func2(1000)
# current time after run
end_time=time.time()
# elapsed time
elapsed_time=end_time-start_time

print(elapsed_time)

print('\n')
# timeit for comparision

import timeit
stat='''
func1(100)
'''
setup='''
def func1(n):
    return print([str(num) for num in range(n)])
'''
print(timeit.timeit(stat,setup,number=1000))

print('\n')

stat2='''
func2(100)
'''
setup2='''
def func2(n):
    return print(list(map(str,range(n))))
'''
print(timeit.timeit(stat,setup,number=1000))