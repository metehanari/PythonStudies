#constructors and other special methods.

class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
        
jonagold = Apple("red","sweet")

print(jonagold.color)

print(jonagold.flavor)
