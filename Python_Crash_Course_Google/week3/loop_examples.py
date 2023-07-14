def count_factors(given_number):
    factor = 1
    count = 1
    
    if given_number == 0:
     return 0
    
    while factor < given_number:
        
        if given_number % factor == 0:
               count += 1
                   
        factor += 1
    
    return count
 

print(count_factors(12))