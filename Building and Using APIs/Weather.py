import requests
import sys
import os

# import the creds that are not being pushed to github
sys.path.insert(1, '../..')
import creds
city_name = 'Orlando'

def get_weather(city, units='metric', api_key=creds.weather_key):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units={units}'
    content = requests.get(url)



print(get_weather(city'Orlando'))
