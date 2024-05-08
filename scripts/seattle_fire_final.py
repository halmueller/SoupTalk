import requests
from bs4 import BeautifulSoup as bs
import json
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy import Point
import sys
import time

def geocode_seattle(address, attempt_count=0, max_attempts=5):
     # Nominatim wants max 1 per second. If we hit a timeout last try, increase the sleep() delay.
    time.sleep(1 + attempt_count*2)
    try:
        timeout = 1 + attempt_count*2
        # extended bounding box for Seattle
        viewbox = [Point(47.8, -122.2), Point(47.4, -122.5)]
        return geocoder.geocode(row_result["address"]+", Seattle, WA", timeout=timeout, viewbox=viewbox, bounded=True)
    except:
        # Could use "except geopy.exc.GeocoderTimedOut", but there are some other exceptions occasionally thrown too
        if attempt_count < max_attempts:
            print("geocode timed out or other exception, retrying", address, file=sys.stderr)
            return geocode_seattle(address, attempt_count=attempt_count+1)
        else:
            print("geocode timed out or other exception, giving up", address, file=sys.stderr)
            return None

URL1 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdApril01.html"
URL2 = "https://raw.githubusercontent.com/halmueller/SoupTalk/develop/html_samples/sfdMarch31.html"
URL3 = "https://web.seattle.gov/sfd/realtime911/getRecsForDatePub.asp?action=Today&incDate=&rad1=des"

page = requests.get(URL1)
# Need 'verify=False' because seattle.gov's certificate isn't picked up by Python. Better fixes than this exist.
# page = requests.get(URL1, verify=False)

soup = bs(page.content, "html.parser")

tables = soup.find_all("table")

geocoder = Nominatim(user_agent="SoupPractice.hal")

# empty dictionary to hold results
incidents_dict = {}
for callRow in tables[3].find_all("tr"):
    fields = callRow.find_all("td")
    # Save incident number to use as key in results dictionary
    incident_number = fields[1].text
    row_result = {
        "date" : fields[0].text,
        # Keep the incident number in the row result, to simplify the final output
        "incident" : fields[1].text,
        # ignore "Level" (fields[2]), don't know what it means
        "units" : fields[3].text,
        "address" : fields[4].text,
        "types" : fields[5].text,
        }
    if callRow.find_all("td", {"class": "closed"}):
        row_result["status"] = "closed"
    else:
        row_result["status"] = "open"

    # In production, I will generally prefer geocoding as a last step, in the database after insertion,
    # especially if only a very small subset of data needs geocoding at each update. For the Seattle Fire
    # data in particular, it's server abuse to reprocess the entire day's results at each 60-second update.
    location = geocode_seattle(row_result["address"])
    # print(incident_number, location, file=sys.stderr)
    if location is not None:
        row_result["latitude"] = location.latitude
        row_result["longitude"] = location.longitude
        if location.raw["name"]:
            row_result["name"] = location.raw["name"]

    # We can have multiple rows for a single incident, if units were added to the response. Combine them here.
    # Optimization opportunity: do this step first, and don't geocode again if we can skip it.
    old_entry = incidents_dict.get(incident_number)
    if old_entry is not None:
        row_result["units"] = f"{row_result['units']} {old_entry['units']}"
        
    incidents_dict[incident_number] = row_result

# We now have a dictionary { incident_number : row_result }
incidents_list = list(incidents_dict.values())
json_out = json.dumps(incidents_list, indent=2)
print(json_out)

