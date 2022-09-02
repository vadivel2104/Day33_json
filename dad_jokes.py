import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json as js


# joke = response.json()
# print(joke)

# import requests
#
# url = "https://dad-jokes.p.rapidapi.com/random/joke"
#
# headers = {
# 	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
# 	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers)
#
# print(response.text)
