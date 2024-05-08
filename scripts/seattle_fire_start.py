import requests
from bs4 import BeautifulSoup as bs


# URL = "https://example.com"
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)

soup = bs(page.content, "html.parser")
print(soup)

results = soup.find(id="ResultsContainer")
print(results.prettify)
