def attempts(n): #define a function
    x = 0 # initialize
    while x < n:
        print("attempt " + str(x + 1)) #print this line as long as x < n and print attempt number
        x+=1

attempts(5)        #output will be 5 attempts