#weather wesite Extension
import argparse
import json
import requests
import sys
import streamlit as st
from configparser import ConfigParser
from urllib import parse, request
from pprint import pp
#from streamlit_card import card

#Base URL the api
BASE_WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

#Note (I am follow the method programming)
#Getting api key
def _get_api_key():
  config = ConfigParser()
  config.read("secrets.ini")
  return config["OpenWeather"]["api_key"]

#Method to create the path pull the data from the base URL
def build_weather_query(city_input, imperial = False):
 api_key = _get_api_key()
 city_name = " ".join(city_input)
 url_encoded_city_name = parse.quote_plus(city_name)
 units = "imperial" if imperial else "metric"
 url = (
 f"{BASE_WEATHER_API_URL}?q={city_input},"
 f"nz&appid={api_key}")
 return url

#This is extract the proper information and put it under one string method
def display_weather_info(weather_data):
 first_L = weather_data['weather']
 second_L = "Weather Condition: "+ first_L[0]['main'] + " <br> Description: " +first_L[0]['description']
 parts = str(second_L)
 return parts

#Getting more information url
def display_weather_hum(weather_data):
 hum = weather_data['main']
 hum_dis = "humidity:" + str(hum['humidity'])
 return hum_dis 

#Method to creating the website
def create_website():

 #Header to the website 
 st.header("LemonWeather", divider = "rainbow")

 #Giving the user the option to install
 option = st.selectbox('Where are you looking for?',('Auckland','Tauranga','Wellington','Hamilton','Christchurch','Rotorua','Queenstown'))

 #Calling the method and combining methods to display
 api_key = _get_api_key() 
 urlss = build_weather_query(option)
 data = requests.get(urlss).json()
 splits = display_weather_info(data)
 hum_des = display_weather_hum(data)

 #Importing css styles into the results
 #Attempting to make the results look like a widget
 #import streamlit.components.v1 as components
 #components.html("<div class="card"><div class="card-body">"+splits+hum_des +"</div></div>")
 col_small,col2 = st.columns([0.4,0.6])
 with col_small:
    with st.container(border=True):
     option2 = st.selectbox("What are you looking:", ('Temperature','Wind Speed'), width=150)
     if(option2 == 'Temperature'):
        st.write(":material/thermostat: Temperature display")
     if(option2 == 'Wind Speed'):
        st.write('Wind speed')

if __name__ == "__main__":

	create_website()
