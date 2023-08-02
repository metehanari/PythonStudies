#list examples

L = ["Michael Jackson", 10.1, 1982,"MJ",1]
print(L[3:5])
#slice a list

L1 = L + ["disco",4]
print(L1)
#concatenate lists

L1.extend(["pop",22])
print(L1)
#extend list is used to add elements to the list

L.append(["pop",22])
print(L)
#append is different from extend as it adds the list as an element to the list

A = ["disco", 10, 1.2]
A[0] = "hard rock"
print(A)
#change the element based on index

del(A[0])
print(A)
#delete the element based on index



print("hard rock".split())
#split the string into a list, space is the default delimiter


print("ad,f,r,rgt,y".split(","))
#split the string into a list, comma is the delimiter


A=["hard rock",10, 1.2]
B = A[:]
#clone the list A and assign it to B