import requests
from bs4 import BeautifulSoup as bs
import json
from geopy.geocoders import Nominatim

URL1 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdApril01.html"
URL2 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdMarch31.html"
page = requests.get(URL1)

soup = bs(page.content, "html.parser")

tables = soup.find_all("table")
# print(len(tables))
# print(tables[3])

geocoder = Nominatim(user_agent="SoupPractice.hal")

# a more Pythonic approach would be a list comprehension
incidents = []
for callRow in tables[3].find_all("tr"):
    fields = callRow.find_all("td")
#    print(fields[4].text)
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
    location = geocoder.geocode(row_result["address"]+", Seattle, WA")
    row_result["latitude"] = location.latitude
    row_result["longitude"] = location.longitude
    # Geocoder timeouts: see https://gis.stackexchange.com/a/184376
    incidents.append(row_result)

# Note: multiple entries for an incident number create multiple list entries.
# print(incidents)

json_out = json.dumps(incidents)
 print(json_out)
