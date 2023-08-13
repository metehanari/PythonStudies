#query string

import requests

url_get = "http://httpbin.org/get" #link to the website

payload = {"name": "Joseph", "ID": "123"} # ?name=Joseph&ID=123 is the query string

r = requests.get(url_get, params=payload) #get the html and store it in r

print(r.json()) #print the json from the website.json file type is a dictionary

r.json()["args"] #print the json from the website.json file type is a dictionary