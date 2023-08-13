#query string

import requests

url_get = "http://httpbin.org/get" #link to the website

payload = {"name": "Joseph", "ID": "123"} # ?name=Joseph&ID=123 is the query string

r = requests.get(url_get, params=payload) #get the html and store it in r

print(r.url) #print the url

print(r.request.body, "||", r.status_code)#print the request body and status code

print(r.text) #print the text from the website

print(r.headers["Content-Type"]) #print the content type from the header
