#writing files "w" mode

Lines = ["This is line A\n","This is line B\n","This is line C\n"] #create a list of lines

with open("C:/Users/HP/Desktop/test3.txt","w") as file1: #this will open the file in write mode
    for line in Lines: #for each line in the list Lines
        file1.write(line) #write the line in the file