#try, except

a = 1

try: 
    b = int(input("Please enter a number to divide a\n "))
    a = a/b
    print("Success a = ", a)
except:
    print("There was an error")
    