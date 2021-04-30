class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("i am a jaguar")
    def eat(self):
        print('i eat humans ')
myAnimal=Animal()
myAnimal.who_am_i()
(myAnimal.eat())

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("dog created")
    
    def who_am_i(self):
        print('i am dog')
    def eat(self):
        print('i eat goo')
mydog=Dog()
mydog.who_am_i()
mydog.eat()
