from PIL import Image
import requests
import matplotlib.pyplot as plt
import json
import urllib.parse as urlparse
from urllib.parse import urlencode
import re

city=input('inter the name of city\n')

parameters_0 = {
    "q": city,
    "appid": "d8aaad5f4b47f70adc98da3406b9021c"
}

response_loc = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=parameters_0)

parameters = {
    "lon": response_loc.json()[0]['lon'],
    "lat": response_loc.json()[0]['lat'],
    "appid": "d8aaad5f4b47f70adc98da3406b9021c"
}

response_for = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response_curr = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response_poll = requests.get("http://api.openweathermap.org/data/2.5/air_pollution", params=parameters)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=False, indent=1)
    print(text)


print("current temperature:",'{:0.0f}'.format(response_curr.json()['main']['temp']-273.15),"C")
print("feels like:",'{:0.0f}'.format(response_curr.json()['main']['feels_like']-273.15),"C")
print("minimum temperature:",'{:0.0f}'.format(response_curr.json()['main']['temp_min']-273.15),"C")
print("maximum temperature:",'{:0.0f}'.format(response_curr.json()['main']['temp_max']-273.15),"C")
print("weather condition:",response_curr.json()['weather'][0]['main'])

icon=response_curr.json()['weather'][0]['icon']
path="".join([icon, "@2x.png"])
url="".join(["http://openweathermap.org/img/wn/", path])

response = requests.get(url,stream=True)
img = Image.open(response.raw)
img.show()

def numbers_to_strings(argument):
    switcher = {
        1: "good",
        2: "satisfactory",
        3: "moderate",
        4: "poor",
        5: "very poor",
    }
    return switcher.get(argument, "nothing")

jprint(response_for.json())
print("air condition:",numbers_to_strings(response_poll.json()['list'][0]['main']['aqi']))
res=[]

times_pattern = r"^(\d{4})-(\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):\d{2}:\d{2}"
dates_pattern = r"^(\d{4})-(\d{2})-(?P<day>\d{2})"
for var in response_for.json()['list']:
   # get year, month and day with regex to create image url
   matches = re.search(times_pattern,var['dt_txt'])
   time = matches.group('hour')
   res.append(time)
   

