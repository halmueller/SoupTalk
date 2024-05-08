import requests
from bs4 import BeautifulSoup as bs


# URL = "https://web.seattle.gov/sfd/realtime911/getRecsForDatePub.asp?action=Today&incDate=&rad1=des"
URL1 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdApril01.html"
URL2 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdMarch31.html"
page = requests.get(URL1)

#print(page.text)

soup = bs(page.content, "html.parser")
#print(soup.prettify)

tables = soup.find_all("table")
print(len(tables))
print(tables[3])

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
    print(row_result)



