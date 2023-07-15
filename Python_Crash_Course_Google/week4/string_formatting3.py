def to_celsius(x):
    return (x - 32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))
    #align the text three spaces to the right --> {:>3}
    #align the text six spaces to the right and 2 decimal spaces --> {:>6.2f} 