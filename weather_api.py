import requests
import json as js
import pandas as pd
import datetime as dt
import os
from twilio.rest import Client


#to read data from contact list

data = pd.read_csv("contact_list.csv")
df = pd.DataFrame(data)
contacts = df[["Name","Phone Number"]].to_dict(orient="records")
# print(contacts)



PARAMETERS = {
    "lat" : 13.0827,
    "lon" : 80.2707,
    "appid" : "2b270e43b626c370acaafb6630335835",
}

URL = "https://api.openweathermap.org/data/2.5/weather?"

response = requests.get(url=URL, params=PARAMETERS)
data = response.json()
current_weather = data["weather"]
# print(current_weather)

condition = [data["description"] for data in current_weather]
# print(condition[0])

#twilio api
account_sid = 'AC62a76ff28762d704c659018522cd33e5'
auth_token = '3140e35ffff8cdad90e7b2cee27eb1b1'
client = Client(account_sid, auth_token)
twilio_number = "+19783092306"


#creating message
for contact in contacts:
    if contact["Name"] == "Vadivel":
        with open("message.txt") as text:
            message = text.read()
            to_number = "+91"+str(contact["Phone Number"])
            name_replaced = message.replace("[contact]",contact["Name"])
            date_replaced = name_replaced.replace("[date]",str(dt.date.today()))
            weather_replaced = date_replaced.replace("[weather]",str(condition[0]))
        print(weather_replaced)
        send_sms = client.messages \
                    .create(
                            body=weather_replaced,
                            from_= twilio_number,
                            to= to_number
                            )
        print(send_sms.sid)
    else:
        break
