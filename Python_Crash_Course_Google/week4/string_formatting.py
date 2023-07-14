name = "Zeynep"

number = len(name) * 4

print("Hello {} your lucky number is {}".format(name,number))
# putting variables to {} 
#format() method deals with TypeErrors.(name=string, number = integer)
#It's not a problem for format() method.


print("Hello {name} your lucky number is {number}".format(name = name,number = len(name) * 5))
#another usage.
 