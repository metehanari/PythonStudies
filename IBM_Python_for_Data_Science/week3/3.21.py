#class example

class Circle(object):
    
    def __init__(self, radius = 3, color = "red"): # constructor with default values
        self.radius = radius # attribute
        self.color = color # attribute
    def add_radius(self, r):# method
        self.radius = self.radius + r 
        return(self.radius)
    def drawCircle(self): # method
        import matplotlib.pyplot as plt # import library 
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color)) # gca = get current axes, fc = face color
        plt.axis('scaled') # equal scaling on both axis
        plt.show() # show the plot
        
c1 = Circle(5,"green")
c1.drawCircle()

dir(c1) # list the data attributes and methods of the object c1