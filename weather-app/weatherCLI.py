#weather cli

import argparse
import json
import requests
import sys
from configparser import ConfigParser
from urllib import parse, request
from pprint import pp

BASE_WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
PADDING = 20
REVERSE = "\033[;7m"
RESET = "\033[0m"

def _get_api_key():
  config = ConfigParser()
  config.read("secrets.ini")
  return config["OpenWeather"]["api_key"]

def read_user_cli_args():
  parser = argparse.ArgumentParser(
  description = "gets weather and temperature information" 
  )

  parser.add_argument(
  "city", nargs="+", type=str, help= "enter the city name"
  )

  parser.add_argument(
  "-i",
  "--imperial",
  action = "store_true", 
  help = "display the termperature in imperial units",
  )

  return parser.parse_args()

def build_weather_query(city_input, imperial = False):
 api_key = _get_api_key()
 city_name = " ".join(city_input)
 url_encoded_city_name = parse.quote_plus(city_name)
 units = "imperial" if imperial else "metric"
 url = (
 f"{BASE_WEATHER_API_URL}?q={city_input},"
 f"nz&appid={api_key}")
 #Making sure the API  URL is showing 
 #print(url)
 return url

def get_weather_data(query_url):
 response = requests.get(query_url).json()
 #data = response.read()
 #weather_apires = requests.get("").json()
 #pp(response) 
 return response

def display_weather_info(weather_data, imperial=False):
 city = weather_data["name"]
 weather_description = weather_data["weather"][0]["description"]
 temperature = weather_data["main"]["temp"]
 print(f"{REVERSE}{city:^{PADDING}}{RESET}", end="")
 print(f"\t{weather_description.capitalize():^{PADDING}}",end=" ",)
 print(f"({temperature}°{'F' if imperial else 'C'})")

if __name__ == "__main__":
  read_user_cli_args()

  city = sys.argv[1]
  imperial = sys.argv[2]
  #print(f"city: {city}" )
  #print(f"imperial:{imperial}")
  #print(city, imperial)
  query_url = build_weather_query(city,imperial)
  weather_data = get_weather_data(query_url)
  display_weather_info(weather_data)
