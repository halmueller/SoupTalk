# SoupTalk

![a python entwined with a soup bowl](Image.png "Beautiful Soup with Python")

Materials for a MaptimeSEA tutorial: using Beautiful Soup to extract geodata from websites. Presented to MaptimeSEA on May 7, 2024.

Use Seattle Fire Department's real-time calls updater,  https://web.seattle.gov/sfd/realtime911/getRecsForDatePub.asp?action=Today&incDate=&rad1=des (or other daily pages from https://web.seattle.gov/sfd/realtime911/) as an example to show how to extract geographic information from a web page, and geocode it.

You'll need a Python3 installation of some sort. Anaconda is a great place to start. See file `prep.txt`.

`CopyPasta.txt` contains URLs that you might want, to save typing them by hand.

`html_samples` has static versions of two captures of the Seattle Fire real-time update, useful for testing because they aren't changing underneath you every 60 seconds.

`scripts` has these files:

- `check_install.py`, to verify that you have all needed Python3 packages installed.
- `nominatim_demo.py`, a standalone demonstration of the Nominatim geocoder.
- `seattle_fire_start.py`, a bare starting point.
- `seattle_fire_phase1.py`, scrapes the page and produces JSON output containing the fire calls.
- `seattle_fire_phase2.py`, extends Phase 1 by geocoding the addresses of the calls.
- `seattle_fire_final.py`, adds some error checking and data simplification.


