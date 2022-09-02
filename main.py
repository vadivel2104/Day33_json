import requests
import json as js

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
print(f"ISS Current Locations:\n{float(data['iss_position']['latitude'])},{float(data['iss_position']['longitude'])}")