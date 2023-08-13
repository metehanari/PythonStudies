#request html

import requests 

url = "https://www.ibm.com/" #link to the website

r = requests.get(url) #get the html and store it in r

print(r.status_code) #print the status code
