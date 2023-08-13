#request-response

import requests

r = requests.get("https://www.ibm.com/")

print(r.request.headers)#print the request headers

print(r.request.body) #print the request body
