# ==========================================
# utils/data.py
# ==========================================

from datetime import datetime


def get_air_quality(aqi):
    """
    Return AQI Status
    """

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 150:
        return "Unhealthy"

    elif aqi <= 200:
        return "Very Unhealthy"

    else:
        return "Hazardous"


def get_air_color(aqi):
    """
    Return AQI Color
    """

    if aqi <= 50:
        return "#16a34a"

    elif aqi <= 100:
        return "#facc15"

    elif aqi <= 150:
        return "#fb923c"

    elif aqi <= 200:
        return "#ef4444"

    else:
        return "#991b1b"


def get_traffic_status(traffic):
    """
    Return Traffic Status
    """

    if traffic <= 30:
        return "Low"

    elif traffic <= 70:
        return "Medium"

    else:
        return "High"


def get_parking_status(parking):
    """
    Return Parking Status
    """

    if parking >= 70:
        return "Available"

    elif parking >= 30:
        return "Limited"

    else:
        return "Full"


def get_city_score(aqi, traffic, parking):
    """
    Calculate Smart City Score
    """

    score = 100

    # AQI

    if aqi > 200:
        score -= 40

    elif aqi > 150:
        score -= 30

    elif aqi > 100:
        score -= 20

    elif aqi > 50:
        score -= 10

    # Traffic

    if traffic > 80:
        score -= 20

    elif traffic > 60:
        score -= 10

    # Parking

    if parking < 20:
        score -= 15

    elif parking < 40:
        score -= 8

    return max(score, 0)


def get_city_data(
    temperature,
    weather,
    aqi,
    traffic,
    electricity,
    parking
):
    """
    Return Complete Dashboard Data
    """

    city = {

        "temperature": temperature,

        "weather": weather,

        "aqi": aqi,

        "air": get_air_quality(aqi),

        "air_color": get_air_color(aqi),

        "traffic": traffic,

        "traffic_status": get_traffic_status(traffic),

        "electricity": electricity,

        "parking": parking,

        "parking_status": get_parking_status(parking),

        "city_score": get_city_score(
            aqi,
            traffic,
            parking
        ),

        "updated": datetime.now().strftime(
            "%d-%m-%Y %I:%M:%S %p"
        )
    }

    return city