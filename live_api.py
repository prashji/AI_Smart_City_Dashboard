import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_aqi(lat, lon):

    print("AQI KEY:", API_KEY)   # <-- Temporary

    url = (
        "https://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}"
        f"&lon={lon}"
        f"&appid={API_KEY}"
    )

    response = requests.get(url)

    print(response.text)         # <-- Temporary

    if response.status_code != 200:
        raise Exception(f"AQI API Error : {response.text}")

    data = response.json()

    return data["list"][0]["main"]["aqi"]



# ============================
# AQI Status
# ============================

def aqi_status(aqi):

    status = {

        1: "🟢 Good",

        2: "🟡 Fair",

        3: "🟠 Moderate",

        4: "🔴 Poor",

        5: "🟣 Very Poor"

    }

    return status.get(aqi, "Unknown")