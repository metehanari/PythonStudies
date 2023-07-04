import requests
from bs4 import BeautifulSoup

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)    #pull url

soup = BeautifulSoup(r.text,"lxml") # pull xml file

price = (soup.find("h4",{"class":"pull-right price"}))  #find h4>class>pull-right price

print(price.string) #dispaly price as string
