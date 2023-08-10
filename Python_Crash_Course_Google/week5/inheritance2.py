#inheritance examples

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm  {name}! {sound}".format(name = self.name,sound = self.sound))
        
class Cow(Animal):# Cow is a child class of Animal
    sound = "Mooo"
    
class Cat(Animal):# Cat is a child class of Animal
    sound = "Meow"



milky = Cow("Milky")
#this instance of Cow class has a name attribute

effy = Cat("Effy")



milky.speak()# inherited from Animal class

effy.speak()
