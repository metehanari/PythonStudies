# username validation checker. If characters length less than 3 characters output is invalid.
# If its longer than 3 characters its okay.
def hint_username(username):
    if len(username)<3:
        print("Invalid name. Must be at least 3 characters.")
    else:
        print("It is valid.")

hint_username("me")