# username validation checker. If characters length less than 3 and longer than 15 characters output is invalid.
# If its longer than 3 and less than 15 characters its okay.
def hint_username(username):
    if len(username)<3:
        print("Invalid name. Must be at least 3 characters.")
    elif len(username)>15:
        print("Too long.Must be less than 15")
    else:
        print("It is valid.")


hint_username("efefefefefefefefefefe")
         