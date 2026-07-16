# ==========================================
# utils/config.py
# ==========================================

# ==========================================
# APPLICATION
# ==========================================

APP_NAME = "AI Smart City Dashboard"

APP_VERSION = "2.0"

AUTHOR = "Shakti Man"

DESCRIPTION = (
    "Real-Time AI Powered Smart City Monitoring Dashboard"
)

# ==========================================
# DEFAULT CITY
# ==========================================

DEFAULT_CITY = "Ahmedabad"

CITY_LIST = [
    "Ahmedabad",
    "Delhi",
    "Mumbai",
    "Surat",
    "Pune",
    "Bangalore"
]

# ==========================================
# WEATHER OPTIONS
# ==========================================

WEATHER_OPTIONS = [
    "Sunny",
    "Cloudy",
    "Rainy",
    "Night"
]

# ==========================================
# PAGE SETTINGS
# ==========================================

PAGE_TITLE = APP_NAME

PAGE_ICON = "🌍"

LAYOUT = "wide"

SIDEBAR_STATE = "expanded"

# ==========================================
# CHART SETTINGS
# ==========================================

CHART_HEIGHT = 340

CHART_TEMPLATE = "plotly_dark"

# ==========================================
# LIMITS
# ==========================================

MIN_TEMP = 10
MAX_TEMP = 50
DEFAULT_TEMP = 32

MIN_AQI = 0
MAX_AQI = 300
DEFAULT_AQI = 70

MIN_TRAFFIC = 0
MAX_TRAFFIC = 100
DEFAULT_TRAFFIC = 35

MIN_ELECTRICITY = 100
MAX_ELECTRICITY = 600
DEFAULT_ELECTRICITY = 320

MIN_PARKING = 0
MAX_PARKING = 100
DEFAULT_PARKING = 75

# ==========================================
# AQI STATUS
# ==========================================

AQI_STATUS = {
    (0, 50): "Good",
    (51, 100): "Moderate",
    (101, 150): "Unhealthy",
    (151, 200): "Very Unhealthy",
    (201, 300): "Hazardous"
}

# ==========================================
# COLORS
# ==========================================

COLORS = {
    "primary": "#2563eb",
    "secondary": "#06b6d4",
    "success": "#16a34a",
    "warning": "#facc15",
    "danger": "#dc2626",
    "background": "#08111f",
    "card": "#111827",
    "text": "#ffffff"
}

# ==========================================
# BACKGROUND IMAGES
# ==========================================

BACKGROUND_IMAGES = {
    "Sunny": "sunny.jpg",
    "Clear": "sunny.jpg",
    "Cloudy": "cloudy.jpg",
    "Clouds": "cloudy.jpg",
    "Rainy": "rainy.jpg",
    "Rain": "rainy.jpg",
    "Night": "night.jpg",
}
# ==========================================
# REFRESH
# ==========================================

AUTO_REFRESH = False

REFRESH_INTERVAL = 5000

# ==========================================
# END
# ==========================================