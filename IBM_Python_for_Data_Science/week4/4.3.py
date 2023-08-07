##file read methods

with open("C:/Users/HP/Desktop/test1.txt","r") as file1: #this will open the file in read mode
        file_stuff = file1.readlines() #this will read the file and store it in a list
    
        print(file_stuff) #this will print the file


print(file_stuff[0]) #this will print the file
