values = [45, 43, 12, 7, 82, 16]    #value list
sum = 0      # initialize values
length = 0   # initialize values

for value in values:
    sum += value       # total of values list numbers
    length += 1        # increase the lenght by 1
    
print("Total sum: " + str(sum) + " Average: " + str(sum / length)) 
# print out the sum and  the average. Average= (sum / list lenght)