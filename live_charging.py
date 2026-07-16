import requests


# ==========================================
# LIVE EV Charging Stations
# ==========================================

def get_live_charging(lat, lon):

    url = (
        "https://api.openchargemap.io/v3/poi/"
        "?output=json"
        f"&latitude={lat}"
        f"&longitude={lon}"
        "&distance=10"
        "&distanceunit=KM"
    )

    try:

        response = requests.get(url, timeout=20)

        data = response.json()

        return len(data)

    except:

        return 0