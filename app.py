import requests
import json
import re

cities = ["London,uk", "Porto,pt", "Paris,fr"]
weather_dict = {}

def city_forecast(city):
    parameters = {
        "q": "city",
        "appid": "d8aaad5f4b47f70adc98da3406b9021c"
    }

    response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=parameters)

    return response.json()

for city in cities:
  weather_dict[city] = city_forecast(city)


#def jprint(obj):
#    text = json.dumps(obj, sort_keys=True, indent=4)
#    print(text)

#print( weather_dict[city])
#print( weather_dict[city]['list'][0]['main']['feels_like'])
def get_day_weather(pred):

  pattern = re.compile("12:\d\d:\d\d")
  t = pattern.search(pred['dt_txt'])

 

day_weather = {}

for city in weather_dict.keys():
  day_weather[city] = list(filter(get_day_weather, weather_dict[city]['list']))

#pattern = re.compile("\d\d:\d\d:\d\d")
#t = pattern.findall(weather_dict[city]['list'][0:1]['dt_txt'])
print( day_weather[city])
#print(t)