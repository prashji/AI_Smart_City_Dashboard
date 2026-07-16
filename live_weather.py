import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("API KEY =", API_KEY)


# ================================
# Live Weather
# ================================

def get_live_weather(city):

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        "&units=metric"
    )

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Weather API Error : {response.text}")

    data = response.json()

    return {

        "temp": data["main"]["temp"],

        "weather": data["weather"][0]["main"],

        "humidity": data["main"]["humidity"],

        "pressure": data["main"]["pressure"],

        "wind": data["wind"]["speed"],

        "lat": data["coord"]["lat"],

        "lon": data["coord"]["lon"]

    }