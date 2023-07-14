message = "A along string with a silly typo" # massage[2] = " " will create an error.strings are immutable.

new_massage = message[:2] + " " + message[3:]  # put a blank instead of "a"

print(new_massage)
