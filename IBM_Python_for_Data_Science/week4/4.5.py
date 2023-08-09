# readlines() method

with open("C:/Users/HP/Desktop/test1.txt","r") as file1: #this will open the file in read mode
        file_stuff = file1.readlines()
        print(file_stuff[:4]) #print the first 4 lines of the file