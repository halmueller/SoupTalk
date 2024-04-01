import requests
from bs4 import BeautifulSoup as bs


# URL = "https://web.seattle.gov/sfd/realtime911/getRecsForDatePub.asp?action=Today&incDate=&rad1=des"
URL = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdMarch31.html"
page = requests.get(URL)

# print(page.text)

soup = bs(page.content, "html.parser")
#print(soup.prettify)

tables = soup.find_all("table")
print(len(tables))
print(tables[3])

#for tag in soup.find_all("table"):
#    print("------------------------------------------------------------------------------------------------")
#    print(len(tuple(tag.children)))
#    print(tag.prettify)
#    for c in tag.children:
#        print(c)

# t1 = soup.find("table")
# t2 = soup.find("table")
# t3 = soup.find("table")
# t4 = soup.find("table")
# t5 = soup.find("table")
# t6 = soup.find("table")
# t7 = soup.find("table")
# t8 = soup.find("table")
# t9 = soup.find("table")
# print(t9.prettify)


