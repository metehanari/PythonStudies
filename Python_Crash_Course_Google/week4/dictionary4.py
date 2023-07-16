#an example about dictionary using

def count_letters(text):
    #define function
    result = {}
    #initalize dictionary with a empty dictionary
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result 

print(count_letters("I am writing something"))