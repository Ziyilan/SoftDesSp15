"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from math import radians, sin, cos, atan2, sqrt

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    address=place_name.replace (" ", "+")
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+address
    response_data = get_json(url)
    data=response_data["results"][0]["geometry"]["location"]
    lat=str(data.get("lat"))
    lng=str(data.get("lng"))
    location=(lat,lng)
    return location



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
 
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat="+latitude+"&lon="+longitude+"&format=json"
    response_data = get_json(url)
    data = response_data["stop"][0]
    name = data.get("stop_name")
    name = str(name.strip("u'"))
    lat = data.get("stop_lat")
    lng = data.get("stop_lon")
    lat=radians(float(lat))
    lng=radians(float(lng))
    latitude=radians(float(latitude))
    longitude=radians(float(longitude))
    deltalat = lat-latitude
    deltalng = lng-longitude
    a = (sin(deltalat/2))**2 + cos(lat) * cos(latitude) * (sin(deltalng/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6373.0 * c
    distance=str(distance)
    return (name, distance)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    data = get_lat_long(place_name)
    return get_nearest_station(data[0], data[1])

print find_stop_near("Fenway Park")