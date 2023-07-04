import requests
from bs4 import BeautifulSoup, Tag

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url) #response

soup = BeautifulSoup(r.text,"lxml") #pull html code as a readable soup

tag = soup.header
#print(tag)
atb = tag.attrs
print(atb["class"])  #display html attributes
