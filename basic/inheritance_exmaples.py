class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Fido")
cat = Cat("Fluffy")

print(dog.name + " says " + dog.speak())   # output: Fido says Woof!
print(cat.name + " says " + cat.speak())   # output: Fluffy says Meow!
