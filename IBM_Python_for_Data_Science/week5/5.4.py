#request-response-html

import requests

url = "https://www.ibm.com/"

r = requests.get(url)

header = r.headers #header info

print(header['date']) #date the request was sent

print(header['Content-Type']) #content type of the request

print(r.encoding) #encoding

print(r.text[:100]) #print the first 100 characters


