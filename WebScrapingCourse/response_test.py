import requests

url = "https://edestek2.kocaeli.edu.tr/my/courses.php"

r = requests.get(url)

print(r.status_code)        



#info responses=100..199
#successful responses=200..299
#redirection messages=300..399
#client error responses=400..499
#server error response=500..599

