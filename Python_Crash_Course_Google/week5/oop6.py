#constructor example.
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return "hi, my name is {}".format(self.name) 


some_person = Person("Effy")  

print(some_person.greeting())