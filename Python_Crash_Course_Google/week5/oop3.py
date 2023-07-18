#instance of class example.

class Cat:
    name = "cat"
    def speak(self):
        print("Meow! I'm {}! Meow!".format(self.name))
        

effy = Cat()

effy.name = "Effy"

effy.speak()



maple = Cat()

maple.name = "Maple"

maple.speak()