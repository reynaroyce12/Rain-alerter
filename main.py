import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')

params = {
    "lat": 10.786730,
    "lon": 76.654793,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=params)
response.raise_for_status()
data = response.json()
hourly_data = data['hourly']
twelve_hour = hourly_data[:12]          # slicing out only 12 hours

will_rain = False
for i in range(len(twelve_hour)):
    if data['hourly'][i]['weather'][0]['id'] < 700:
        zeroth_data = data['hourly'][i]['weather'][0]['id']
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Don't forget the umbrella! ☂️",
            from_='+12284324829',
            to='+919656817180'
        )

    print(message.status)
