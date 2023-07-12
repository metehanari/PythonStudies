x=4
if x != 0: #if x=0 while loop will be inf. This "if" line breaks the inf loop.
    while x % 2 == 0:
        x = x /2
        print(x)

# solution 2 => while x!=0 and x%2==0: