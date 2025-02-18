import requests
from bs4 import BeautifulSoup as bs


URL1 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdApril01.html"
URL2 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdMarch31.html"
URL3 = "https://web.seattle.gov/sfd/realtime911/getRecsForDatePub.asp?action=Today&incDate=&rad1=des"
page = requests.get(URL1)

print(page.text)

soup = bs(page.content, "html.parser")
print(soup.prettify)
