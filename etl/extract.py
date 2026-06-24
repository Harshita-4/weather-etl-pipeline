import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

CITIES = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"]

def extract_weather():
    weather_data = []
    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data.append(response.json())
        else:
            print(f"Failed for {city}: {response.status_code}")
    return weather_data