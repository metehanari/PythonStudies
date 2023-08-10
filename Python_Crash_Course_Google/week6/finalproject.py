#sorted key

names = ["Carlos", "Ray", "Alex", "Kelly"]

print(sorted(names, key= len)) 
#sorts by length of string.
#key is a function that is called on each element before sorting
