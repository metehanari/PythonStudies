import requests
from bs4 import BeautifulSoup
import re #regular expression


url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

data = soup.find_all(string = re.compile("Galaxy")) #exact search with "re" library
 
for i in data:
    print(i.text)


