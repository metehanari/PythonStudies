#functions

def PinkFloyd():
    global ClaimedSales
    ClaimedSales = "45 Million"
    return ClaimedSales
# global variable is a variable that is defined outside of a function scope
 
PinkFloyd()
#calling the function

print(ClaimedSales)
# printing the global variable

