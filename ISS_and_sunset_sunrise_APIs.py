# -*- coding: utf-8 -*-

""" Sunset and sunrise times API 

Endpoint or url: https://api.sunrise-sunset.org/json

Parameters
lat (float): Latitude in decimal degrees. Required.
lng (float): Longitude in decimal degrees. Required.
date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. If not present, date defaults to current date. Optional.
callback (string): Callback function name for JSONP response. Optional.
formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.


Usage limits and attribution
The sunrise and sunset API can be used free of charge. You may not use this API in a manner that exceeds reasonable request volume, constitutes excessive or abusive usage. We require that you show attribution to us with a link to our site.
"""


"""
These are the following modules/packages you'll need
to install and import:

"""
import requests
from datetime import datetime
import smtplib
import time


response = requests.get("https://api.sunrise-sunset.org/json")
response.raise_for_status()
data = response.json()
print(data)

"""
results

print(data)
{'results': {'sunrise': '5:40:32 AM', 'sunset': '5:49:29 PM', 'solar_noon': '11:45:00 AM', 'day_length': '12:08:57', 'civil_twilight_begin': '5:20:38 AM', 'civil_twilight_end': '6:09:23 PM', 'nautical_twilight_begin': '4:56:15 AM', 'nautical_twilight_end': '6:33:45 PM', 'astronomical_twilight_begin': '4:31:51 AM', 'astronomical_twilight_end': '6:58:09 PM'}, 'status': 'OK'}


"""






""" Create parameters using python dictionary and strings with info 
from the sunrise-sunset website and lat and long from https://www.latlong.net/"""

""" Lets create lat and lng as MY_CONSTANT as floating numbers 
and using params within request.get via dictionaries { } 
used for defining 'parameters' """


MY_LAT = 55.864239
MY_LONG = -4.251806

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

""" 
results

{'results': {'sunrise': '6:54:02 AM', 'sunset': '5:09:59 PM', 
'solar_noon': '12:02:01 PM', 'day_length': '10:15:57', 
'civil_twilight_begin': '6:18:13 AM', 'civil_twilight_end': '5:45:48 PM', 
'nautical_twilight_begin': '5:35:17 AM', 'nautical_twilight_end': '6:28:45 PM', 
'astronomical_twilight_begin': '4:52:20 AM', 
'astronomical_twilight_end': '7:11:41 PM'}, 
 'status': 'OK'}

"""

""" Check for exceptions using the following command line"""
# Make the API request
# Check if the status code is 404
# Process the response here
# The following command lines have to be run altogether
          
          
try:
    response= requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    if response.status_code == 404:
        print("404 - Resource Not Found")
    else:
        data_1 = response.json()
        print(data_1)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")

except Exception as e:
    print(f"An unexpected error occured: {e}")
    
"""{'results': {'sunrise': '6:54:02 AM', 
'sunset': '5:09:59 PM', 
'solar_noon': '12:02:01 PM', 
'day_length': '10:15:57', 
'civil_twilight_begin': '6:18:13 AM', 
'civil_twilight_end': '5:45:48 PM', 
'nautical_twilight_begin': '5:35:17 AM', 
'nautical_twilight_end': '6:28:45 PM', 
'astronomical_twilight_begin': '4:52:20 AM', 
'astronomical_twilight_end': '7:11:41 PM'}, 'status': 'OK'}"""

    
# Lets deliberately make an error by incrrecting the url

try:
    response= requests.get("https://api.sunri-s.org/json", params=parameters)
    response.raise_for_status()
    if response.status_code == 404:
        print("404 - Resource Not Found")
    else:
        data_1 = response.json()
        print(data_1)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")

except Exception as e:
    print(f"An unexpected error occured: {e}")
    
"""Request error occurred: HTTPSConnectionPool(host='api.sunri-s.org', port=443): 
    Max retries exceeded with url: /json?lat=55.864239&lng=-4.251806 
    (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object 
        at 0x000001F3E06731D0>: Failed to establish a new connection: 
    [Errno 11001] getaddrinfo failed'))"""
    
# Lets view the JSON data in a nice format by using sample request via JSON Viewer plugin on Chrome. This can be downloaded and installed.
"""
https:// end point ? parameter_name=value & parameter_name=value

then copy and paste it into the search bar on chrome

"""

# We can also retrieve sunrise and sunset only so let's define each
sunrise = data_1["results"]["sunrise"]
sunset = data_1["results"]["sunset"]

print(sunrise)
print(sunset)


# Testing out datetime module/package
time_now = datetime.now()
print(time_now)

""" Modify the API call:
    turn off the formatting
    and time in the 24-hour style
    so that we can see 12-hour format instead
    
    by adding one more parameter
    to the following dictionary which 
    is contained in requests.get within params function"""
    
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


try:
    response= requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    if response.status_code == 404:
        print("404 - Resource Not Found")
    else:
        data_1 = response.json()
        print(data_1)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")

except Exception as e:
    print(f"An unexpected error occured: {e}")

"""{'results': {'sunrise': '2023-10-19T06:54:02+00:00', 
'sunset': '2023-10-19T17:09:59+00:00', 
'solar_noon': '2023-10-19T12:02:01+00:00', 
'day_length': 36957, 'civil_twilight_begin': '2023-10-19T06:18:13+00:00', 
'civil_twilight_end': '2023-10-19T17:45:48+00:00', 
'nautical_twilight_begin': '2023-10-19T05:35:17+00:00', 
'nautical_twilight_end': '2023-10-19T18:28:45+00:00', 
'astronomical_twilight_begin': '2023-10-19T04:52:20+00:00', 
'astronomical_twilight_end': '2023-10-19T19:11:41+00:00'}, 
'status': 'OK'}"""
                                  
""" Lets compare hours from sunset API against 
hours from our datetime API 

Need to isolate the hour number from each of these for comparison
by using Python Split();
split the string, using comma, followed by a space, as a separator

or use a hash or pound character as a separator

For instance we split the "T" between 
date and time from the following: 
    2023-10-19T17:09:59+00:00
         0            1

We can split further with index number

"""
print(sunrise.split("T"))

"""print(sunrise.split("T"))
['6:54:02 AM']"""

print(sunrise.split("T")[0].split(":"))

"""print(sunrise.split("T")[0].split(":"))
          ['6', '54', '02 AM']

Index number -3    -2    -1
"""

print(sunrise.split("T")[0].split(":")[-1])

"""print(sunrise.split("T")[0].split(":")[-1])
            02 AM    """


""" Lets get the hour only so
          ['6', '54', '02 AM']

Index number -3    -2    -1

Lets put -3
"""

           
print(sunrise.split("T")[0].split(":")[-3])

"""
print(sunrise.split("T")[0].split(":")[-3])
        6

We got the actual hour number ^
"""

"""

Let's use the command line above to find and compare
the sunrise and sunset hours against
each other

"""

sunrise = int(data_1["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data_1["results"]["sunset"].split("T")[1].split(":")[0])


print(sunrise)
print(sunset)
print(time_now.hour)
"""
print(sunrise)
06

print(sunset)
17

"""
print(time_now.hour)

"""
print(time_now.hour)
21

"""



"""IF ISS is close to my current position
and it is currently dark
then send me an email to tell me to look up.
BONUS: run the code every 60 seconds

ISS latitude and longitude are both floating numbers
sunrise and sunset are both integers

In terms of margin of error:
    your position is within +5 or -5 degrees of the ISS position
"""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data)

"""
print(data)
{'timestamp': 1697750314, 
 'message': 
 'success', 
 'iss_position': {'latitude': '14.9639', 
  'longitude': '95.3359'}}

"""

iss_latitude= float(data["iss_position"]["latitude"])
iss_longitude= float(data["iss_position"]["longitude"])

# I'm based in Glasgow
MY_LAT = 55.864239
MY_LONG = -4.251806


"""My position within +5 or -5 degrees of the iss position"""

# if 50 <= iss_latitude <= 60 and -9 <= iss_longitude <= 1
 
if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longtitude <= MY_LONG+5:
    

# I'm based in [insert city name]
MY_LAT = 55.0
MY_LONG = -4.0

""" Let's create a function now that we've figured out what to make 
we'll need to find if the ISS is close to our position
and whether its night time or not
and send us an email to tell us to look up

as bonus we can 'while' loop function for the email

"""

# We can then use smtplib module/package for the following code before we write a couple of functions
MY_EMAIL = "your email"
MY_PASSWORD = "your password"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
     
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longtitude <= MY_LONG+5:
        return True
    

def is_night():
    parameter: {
        "lat": MY_LAT,
        "lng": MY_LONG,
        formatted: 0,
        }
    
    response = request.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data= response.json()
    
    sunrise = int(data_1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_1["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    
if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addr=MY_EMAIL,
        msg="Subject: Look Up \n\n The ISS is above you in the sky."
        )

""" Lets put the email statement into a loop"""

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
     
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longtitude <= MY_LONG+5:
        return True
    

def is_night():
    parameter: {
        "lat": MY_LAT,
        "lng": MY_LONG,
        formatted: 0,
        }
    
    response = request.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data= response.json()
    
    sunrise = int(data_1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_1["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addr=MY_EMAIL,
            msg="Subject: Look Up \n\n The ISS is above you in the sky."
            )