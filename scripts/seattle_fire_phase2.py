import requests
from bs4 import BeautifulSoup as bs
import json

URL1 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdApril01.html"
URL2 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdMarch31.html"
page = requests.get(URL1)

soup = bs(page.content, "html.parser")

tables = soup.find_all("table")

geolocator = Nominatim(user_agent="SoupPractice.hal")

# a more Pythonic approach would be a list comprehension
incidents = []
for callRow in tables[3].find_all("tr"):
    fields = callRow.find_all("td")
    row_result = {
        "date" : fields[0].text,
        "incident" : fields[1].text,
        # ignore Level, don't know what it means
        "units" : fields[3].text,
        "address" : fields[4].text,
        "types" : fields[5].text,
        }
    if callRow.find_all("td", {"class": "closed"}):
        row_result["status"] = "closed"
    else:
        row_result["status"] = "open"
    incidents.append(row_result)

print(incidents)



