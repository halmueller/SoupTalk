# SoupTalk

Materials for a MaptimeSEA tutorial: using Beautiful Soup to extract geodata from websites. Presented to MaptimeSEA on May 7, 2024.

![a python entwined with a soup bowl](Image.png "Beautiful Soup with Python")

In this tutorial, we used Seattle Fire Department's real-time calls updateras an example to show how to extract geographic information from a web page, and geocode it.
- Today's live page: https://web.seattle.gov/sfd/realtime911/getRecsForDatePub.asp?action=Today&incDate=&rad1=des
- Past daily pages: https://web.seattle.gov/sfd/realtime911/

You'll need a Python3 installation of some sort. Anaconda is a great place to start. See file `prep.txt`.

`CopyPasta.txt` contains URLs that you might want, to save typing them by hand.

`conda-cheatsheet.pdf` comes from the Anaconda project, duplicated here for convenience.

`html_samples/` has static versions of two captures of the Seattle Fire real-time update, useful for testing because they aren't changing underneath you every 60 seconds.

`scripts/` has these files:
- `check_install.py`, to verify that you have all needed Python3 packages installed.
- `nominatim_demo.py`, a standalone demonstration of the Nominatim geocoder.
- `seattle_fire_start.py`, a bare starting point.
- `seattle_fire_phase1.py`, scrapes the page and produces JSON output containing the fire calls.
- `seattle_fire_phase2.py`, extends Phase 1 by geocoding the addresses of the calls.
- `seattle_fire_final.py`, adds some error checking and data simplification.

## Sample output

```
[
  {
    "date": "4/1/2024 1:04:18 AM",
    "incident": "F240044331",
    "units": "A2",
    "address": "211 PINE ST",
    "types": "Aid Response",
    "status": "open",
    "latitude": 47.6102707,
    "longitude": -122.3393473855836,
    "name": "Haight Building"
  },
  {
    "date": "4/1/2024 1:01:48 AM",
    "incident": "F240044330",
    "units": "B7 E32 E36 L11",
    "address": "4100 SW EDMUNDS ST",
    "types": "AFA4 - Auto Alarm 2 + 1 + 1",
    "status": "open",
    "latitude": 47.5594406,
    "longitude": -122.38490160392345
  },
  {
    "date": "4/1/2024 12:57:41 AM",
    "incident": "F240044329",
    "units": "E39",
    "address": "3040 Ne 127th St",
    "types": "Illegal Burn",
    "status": "closed",
    "latitude": 47.7216443,
    "longitude": -122.2948379,
    "name": "Tweedy and Popp"
  },
  {
    "date": "4/1/2024 12:48:22 AM",
    "incident": "F240044327",
    "units": "E29",
    "address": "3038 64th Ave Sw",
    "types": "Aid Response",
    "status": "open",
    "latitude": 47.576859999999996,
    "longitude": -122.41423044775647
  },
```

