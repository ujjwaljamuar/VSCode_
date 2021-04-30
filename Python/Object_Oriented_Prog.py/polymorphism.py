class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says Woof!"
class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says Meow!"
    
niko=Dog('Niko')
Felix=Cat("Felix")
print(niko.speak())
print(Felix.speak())

for pet in [niko,Felix]:
    print(type(pet))
    print(pet.speak())
def pet_speak(pet):
        print(pet.speak())
pet_speak(niko)

class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError('subclass must implement this abstract method')
class Dog(Animal):
    def speak(self):
        return self.name+ "says woof"
class Dog(Animal):
    def speak(self):
        return self.name+ "says meow"
fido=Dog('Fido')
isis=Cat('Isis')
print(fido.speak())