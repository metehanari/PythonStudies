#constructor example. memory position of object.

from turtle import goto


class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
        
jonagold = Apple("red", "sweet")

print(jonagold.color)
# red

print(jonagold)
# memory position
#<__main__.Apple object at 0x000001D5A52F7690>
