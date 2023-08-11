# writing files "a" mode. a stands for append. This will append the new lines to the end of the file.

with open("C:/Users/HP/Desktop/test3.txt","a") as file1: #this will open the file in append mode
    file1.write("This is line D\n") #write the line in the file