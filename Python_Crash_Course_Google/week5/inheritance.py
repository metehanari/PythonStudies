#inheritance

class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
#Fruit is a parent class.       
 
class Apple(Fruit):
    pass

class Grape(Fruit):
    pass
# Apple and Grape are siblings. 



fuji = Apple("red", "sweet")

print(fuji.color)


chardonnay = Grape("green", "sour")

print(chardonnay.color)