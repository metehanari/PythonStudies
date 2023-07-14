#if you want to change the old domain to new one.this example about this.
def replace_domain(email, old_domain,new_domain):  
    #define function.
    if "@" + old_domain in email: 
        # if @ sign and old domain are in email address.
        index = email.index("@" + old_domain) 
        # find the index of "@.....com" part.
        new_email = email[:index] + "@" + new_domain 
        # slice "@...com" part, add @, add new domain.
        return print(new_email) 
    # return new email address.
    return email 
# if it doesn't contain old domain. return email address.

replace_domain("metehanari1@gmail.com","gmail.com", "blabla.com")

