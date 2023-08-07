#with open is a better way to open a file cause it closes the file automatically.

with open("C:/Users/HP/Desktop/test1.txt","r") as file1: #this will open the file in read mode
        file_stuff = file1.read() #this will read the file
    
        print(file_stuff) #this will print the file
        

print(file1.closed) #this will check if the file is closed or not

file_stuff

file_stuff.readlines()