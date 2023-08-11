#copy file

with open("C:/Users/HP/Desktop/test3.txt","r") as readfile:
    with open("C:/Users/HP/Desktop/test4.txt","w") as writefile:
        for line in readfile:
            writefile.write("[copy]" + line)