###get_congress.py

#This code simply downloads the latest GovTrack.us data and stores it as a JSON object

import urllib
import json
import os

#creates the directory /congressDB for the json object if not present
try:
    os.makedirs('./congressDB')
except OSError:
    pass

#downloads the object
allCongress = urllib.urlretrieve('https://www.govtrack.us/api/v2/role?current=true&limit=600', "congressDB/congress.txt")
