def to_celsius(x):   #define a celsius converter formula
    return (x - 32) * 5 / 9

for x in range(0, 101, 10):  
    # print out the values 10 by 10 zero to 100
    print(x , to_celsius(x)) 
    
    