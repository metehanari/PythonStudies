pets = "Cats & Dogs"

index1 = pets.index("&") # index() is a method. It gives the index of substring.
print(index1) # 5

index2 = pets.index("Dog")
print(index2) # 7



print("Cats" in pets) # True # we can use "in" for check the substrings in the string

print("Birds" in pets) # False 