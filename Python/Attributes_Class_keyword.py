#creating a class
class Dog():
    # Class object Atrribute
    #same for any instance of a class
    species='Mammal'


    def __init__ (self,breed,name):   #__init_- act as a constructor and self is the instance of the class
        #Attribute
        #We take an attribute
        # Assign it using self.attribute_name
        self.breed=breed
        self.name=name


    def bark(self,number):
         print(f"WOOF! MY name is {self.name} and the number is {number}.")
mydog=Dog('Huskie','CHUtiya')
print(mydog.species)
print(mydog.name)
print(mydog.breed)
print(mydog.bark('12'))

print('\n')


class Circle():
    pi=3.14
    def __init__(self,radius=2):
        self.radius=radius
        self.area=radius*radius*Circle.pi
    def get_circumference(self):
        return self.radius*Circle.pi*2
my_circle=Circle(30)  #you can override it from here from default value
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)