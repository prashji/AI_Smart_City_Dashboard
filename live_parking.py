import requests


# ==========================================
# LIVE PARKING (OpenStreetMap Overpass API)
# ==========================================

def get_live_parking(lat, lon):

    query = f"""
    [out:json];

    node
      ["amenity"="parking"]
      (around:5000,{lat},{lon});

    out;
    """

    url = "https://overpass-api.de/api/interpreter"

    try:

        response = requests.post(
            url,
            data=query,
            timeout=20
        )

        data = response.json()

        parking_count = len(data["elements"])

        return parking_count

    except:

        return 0