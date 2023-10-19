# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 00:50:31 2023

@author: Hafiy
"""

""" International Space Station
Current Location using their API.

We'll automate the following code to check their current location """

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data)

data = response.json()["iss_position"]["longitude"]
data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

""" 
From print() above

{'timestamp': 1697753844, 'message': 'success', 'iss_position': {'latitude': '-46.3945', 'longitude': '-55.5843'}}

{'timestamp': 1697753844, 'message': 'success', 'iss_position': {'latitude': '-46.3945', 'longitude': '-55.5843'}}

('-55.5843', '-46.3945')


"""