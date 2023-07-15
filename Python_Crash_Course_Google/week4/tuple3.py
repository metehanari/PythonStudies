#an example about tuple and list.

def full_emails(people):
    result =[]
    for email,name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_emails([("mete@example.com","Metehan Ari"),("zip@example.com","Zeynep Irem Peker")]))
