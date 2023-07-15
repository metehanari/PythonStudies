#counting the number of characters in animals list.
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
    
print("Total character: {}, Average length: {}".format(chars,chars/len(animals)))