#recursion example.this function calls itself repeatedly.
def factorial(n):
    if n < 2: #base case
        return 1
    return n * factorial(n - 1) #recursive case

print(factorial(4))


############################recursive function structure###############

# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)