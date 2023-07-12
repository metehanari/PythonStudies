def add_table(given_number):
    number = 1
    sum = 1
    while number <=5:
        sum = given_number + number
        if sum > 20:
            print("Stop!")
            break 
        
        
        print(str(given_number), '+', str(number),'=',str(sum))    
        number+=1
    
add_table(1)    