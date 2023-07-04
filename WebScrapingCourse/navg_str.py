import requests
from bs4 import BeautifulSoup

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)


soup = BeautifulSoup(r.text,"lxml")

tag = soup.div.p.string
print(tag)