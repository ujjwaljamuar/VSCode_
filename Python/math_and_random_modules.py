import math

value=4.35
print(math.floor(value)) #prints lower round fig value ie 4
print(math.ceil(value))  # prints uppper round fig value ie 5
print(round(4.3))   # prints round fig ie 4
print(round(4.5)) # if the value is in middle then it will print out the nearest even value ie 4
print(round(5.5)) # if the value is in middle then it will print out the nearest even value ie 6
print(round(4.6)) # round value ie 5
print(math.pi)
print(math.e)
print(math.log(math.e)) # math.e is in base
print(math.log(100,10))  #math.log(num,base)
print(math.sin(45))
print(math.degrees(math.pi/2))
print(math.radians(180))

print('\n')
import random
print(random.randint(0,100))

# set a seed
random.seed(101)
print(random.randint(0,100))

print(random.uniform(a=0,b=100))

print(random.gauss(mu=0,sigma=1))