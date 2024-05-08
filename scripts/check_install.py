import requests
from bs4 import BeautifulSoup as bs
from geopy.geocoders import Nominatim
import json

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text)

soup = bs(page.content, "html.parser")
#print(soup)

print("installation correct")
