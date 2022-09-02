import requests
import json as js
MY_LAT = 13.0827
MY_LONG = 80.2707

PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=PARAMETERS)
response.raise_for_status()