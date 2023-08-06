#create class and method

class Circle(object):
    
    def __init__(self, radius, color): # constructor
        self.radius = radius # attribute
        self.color = color # attribute
    def add_radius(self, r):# method
        self.radius = self.radius + r 
        return(self.radius)
    
    
c1 = Circle(5,"green")
# this is an instance of the class Circle

c1.add_radius(4)
# this is a method of the class Circle

