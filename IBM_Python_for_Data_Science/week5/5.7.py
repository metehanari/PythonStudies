#post

import requests

url_post = "http://httpbin.org/post" #link to the website

payload = {"name": "Joseph", "ID": "123"} 

r_post = requests.post(url_post, data=payload) #post the html and store it in r

print(r_post.url)

print(r_post.request.body)

print(r_post.json()["form"])
