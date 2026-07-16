# ==========================================
# utils/header.py
# ==========================================

from datetime import datetime


# ==========================================
# DATE & TIME
# ==========================================

def get_header(city=None):
    """
    Returns current date and time.
    city parameter optional hai taaki purana app.py bhi work kare.
    """

    now = datetime.now()

    date = now.strftime("%d %B %Y")
    time = now.strftime("%I:%M:%S %p")

    return date, time


# ==========================================
# DAY NAME
# ==========================================

def get_day():

    return datetime.now().strftime("%A")


# ==========================================
# FULL DATE
# ==========================================

def get_full_date():

    return datetime.now().strftime(
        "%A, %d %B %Y"
    )


# ==========================================
# LAST UPDATED
# ==========================================

def get_last_updated():

    return datetime.now().strftime(
        "%I:%M:%S %p"
    )


# ==========================================
# HEADER INFORMATION
# ==========================================

def get_dashboard_header(city_name):

    now = datetime.now()

    return {

        "city": city_name,

        "date": now.strftime("%d %B %Y"),

        "time": now.strftime("%I:%M:%S %p"),

        "day": now.strftime("%A"),

        "updated": now.strftime(
            "%d-%m-%Y %I:%M:%S %p"
        )

    }


# ==========================================
# GREETING
# ==========================================

def get_greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "🌅 Good Morning"

    elif hour < 17:
        return "☀️ Good Afternoon"

    elif hour < 20:
        return "🌇 Good Evening"

    else:
        return "🌙 Good Night"