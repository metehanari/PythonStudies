#logic operators

not True
#not operator returns the opposite of the operand

A = False
B = True
A and B
# and operator returns true if both operands are true



album_year = 1983

if (album_year < 1980) or (album_year > 1989):
    print("The album was made in the 70's or 90's")
else:
    print("The album was made in the 1980's")