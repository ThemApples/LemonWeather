#weather wesite Extension
import argparse
import json
import requests
import sys
import streamlit as st
from configparser import ConfigParser
from urllib import parse, request
from pprint import pp


BASE_WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

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
 return url

def display_weather_info(weather_data):
 first_L = weather_data['weather']
 second_L = "Weather Condition: "+ first_L[0]['main'] + " Description: " +first_L[0]['description']
 print(second_L)
 parts = str(second_L)
 return parts

def create_website():
 st.header("This is basic website", divider = "rainbow")
 option = st.selectbox('Where are you looking for?',('Auckland','Tauranga','Wellington','Hamilton','Christchurch','Rotorua','Queenstown'))

 api_key = _get_api_key() 
 st.write("this is result", option)
 urlss = build_weather_query(option)
 data = requests.get(urlss).json()
 splits = display_weather_info(data)
 st.write(splits)

if __name__ == "__main__":

	create_website()
