#list comprehension
multiples = []
for x in range(1,10 + 1):
    multiples.append(x * 7)

print(multiples)

###############
# we can do this in just one line like this.
multiples2 = [x * 7 for x in range(1,11)]
print(multiples2)