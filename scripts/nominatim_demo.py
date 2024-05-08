from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent="SoupTalk_add_your_name")

# TPC Ballard
# 5101 14th Ave NW
# Suite 201
# Seattle, WA 98103

location1 = geocoder.geocode("5101 14th Avenue NW")
print("address")
print(location1.address)
print("lat lon")
print((location1.latitude, location1.longitude))
print("raw")
print(location1.raw)
# Note the extra info returned ("Great Notion")

print("--------")
location2 = geocoder.geocode("5101 14th Avenue NW, Seattle, WA")
print(location2.address)
print((location2.latitude, location2.longitude))
print(location2.raw)

# Can also constrain to a lat/lon "rectangle"
