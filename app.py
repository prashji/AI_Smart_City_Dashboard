import streamlit as st
from utils.map import live_city_map

from utils.config import (
    APP_NAME,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE,
    BACKGROUND_IMAGES
)

from utils.theme import load_css, set_background

from utils.sidebar import premium_sidebar

from utils.navbar import navbar

from utils.data import get_city_data

from utils.header import get_header, get_greeting, get_dashboard_header

from utils.ai import get_ai_recommendation

from utils.cards import premium_cards

from utils.map import live_city_map

from utils.map import live_city_map

from utils.live_parking import get_live_parking

from utils.live_charging import get_live_charging

from utils.assistant import ai_panel

from streamlit_autorefresh import st_autorefresh

st_autorefresh(

    interval=60000,

    key="refresh"
)
from utils.live_weather import get_live_weather
from utils.live_api import get_aqi, aqi_status
from utils.chatbot import ask_ai



# Charts
from utils.charts import (
    traffic_chart,
    pollution_chart,
    electricity_chart,
    parking_chart,
    temperature_chart,
    traffic_trend_chart,
    aqi_trend_chart
)

st.set_page_config(
    page_title=APP_NAME,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE
)

load_css()

# ==========================================
# Sidebar
# ==========================================

city_name, weather, temperature, aqi, traffic, electricity, parking = premium_sidebar()

# ==========================================
# Live Weather
# ==========================================

weather_data = get_live_weather(city_name)

temperature = weather_data["temp"]
weather = weather_data["weather"]
lat = weather_data["lat"]
lon = weather_data["lon"]

# ==========================================
# Live AQI
# ==========================================

aqi = get_aqi(lat, lon)
aqi_text = aqi_status(aqi)

# ==========================================
# Live Parking
# ==========================================

parking = get_live_parking(lat, lon)

# ==========================================
# Live EV Charging
# ==========================================

charging = get_live_charging(lat, lon)

# Background


set_background(weather)

with st.spinner("Updating Live City Data..."):
    city = get_city_data(
        temperature,
        weather,
        aqi,
        traffic,
        electricity,
        parking
    )

today, current_time = get_header()

greeting = get_greeting()
header = get_dashboard_header(city_name)

recommendations = get_ai_recommendation(city)

st.info(f"{greeting} 👋 Welcome to the AI Smart City Dashboard")

st.markdown(f"### 📌 {header['day']} — Last updated: {header['updated']}")


col1, col2, col3 = st.columns([2, 1, 1])

with col1:

    st.markdown(f"""
    <div class="info-card">
        <h4>🏙 Selected City</h4>
        <h2>{city_name}</h2>
        <p>Current Weather : {weather}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="info-card">
        <h4>📅 Date</h4>
        <h2>{today}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="info-card">
        <h4>🕒 Time</h4>
        <h2>{current_time}</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

premium_cards(city)


weather_icons = {
    "Sunny": "☀️",
    "Cloudy": "☁️",
    "Rainy": "🌧️",
    "Night": "🌙"
}

st.markdown(f"""
<div class="info-card">

<h3>{weather_icons.get(weather, '🌤️')} Current Weather</h3>

<h2>{weather}</h2>

<p><strong>Temperature:</strong> {city['temperature']} °C</p>

<p><strong>Air Quality:</strong> {aqi_text}</p>

<p><strong>Last AQI:</strong> {city['aqi']}</p>

</div>
""", unsafe_allow_html=True)


st.markdown(f"""
<div class="info-card">

<h3>⚡ EV Charging Stations</h3>

<h1>{charging}</h1>

<p>Nearby (10 KM)</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown("## 📊 Live Analytics")

row1_col1, row1_col2 = st.columns(2)



with row1_col1:

    st.plotly_chart(
        temperature_chart(city["temperature"]),
        use_container_width=True
    )


with row1_col2:

    st.plotly_chart(
        traffic_chart(city["traffic"]),
        use_container_width=True
    )



row2_col1, row2_col2 = st.columns(2)

with row2_col1:

    st.plotly_chart(
        pollution_chart(city["aqi"]),
        use_container_width=True
    )

with row2_col2:

    st.plotly_chart(
        electricity_chart(city["electricity"]),
        use_container_width=True
    )



st.markdown("## 🅿 Parking Analysis")

st.plotly_chart(
    parking_chart(city["parking"]),
    use_container_width=True
)

st.markdown("---")


st.markdown("## 📈 Weekly Analytics")

col1,col2 = st.columns(2)

with col1:

    st.plotly_chart(

        traffic_trend_chart(),

        use_container_width=True

    )

with col2:

    st.plotly_chart(

        aqi_trend_chart(),

        use_container_width=True

    )


st.markdown(f"""
### 🗺 Live Location

📍 {city_name}

Latitude : {lat:.4f}

Longitude : {lon:.4f}
""")

st.markdown("## 🗺 Live Map & AI Assistant")

left, right = st.columns([2,1])

with left:

    live_city_map(

        city_name,

        lat,

        lon

    )

with right:
    ai_panel(recommendations)




st.markdown("## 📈 Live City Status")

status1, status2, status3 = st.columns(3)

with status1:

    st.markdown(f"""
    <div class="info-card">

    <h3>🌫 Air Quality</h3>

    <h2>{city['air']}</h2>

    <p>AQI : {city['aqi']}</p>

    </div>
    """, unsafe_allow_html=True)

with status2:

    st.markdown(f"""
    <div class="info-card">

    <h3>🚦 Traffic</h3>

    <h2>{city['traffic_status']}</h2>

    <p>{city['traffic']}%</p>

    </div>
    """, unsafe_allow_html=True)

with status3:

    st.markdown(f"""
    <div class="info-card">

    <h3>🅿 Parking</h3>

    <h2>{city['parking_status']}</h2>

    <p>{city['parking']}%</p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("---")



st.markdown("## ⚡ Resource Utilization")

st.write("Electricity Usage")
st.progress(city["electricity"] / 600)

st.write("Traffic Density")
st.progress(city["traffic"] / 100)

st.write("Parking Availability")
st.progress(city["parking"] / 100)

st.write("Air Pollution Level")
st.progress(city["aqi"] / 300)

st.markdown("<br>", unsafe_allow_html=True)



st.markdown("## 📋 Smart City Summary")

summary1, summary2 = st.columns([2, 1])

with summary1:

    st.markdown(f"""
    <div class="info-card">

    <h3>🏙 City Overview</h3>

    <table width="100%">

    <tr>
        <td><b>City</b></td>
        <td>{city_name}</td>
    </tr>

    <tr>
        <td><b>Weather</b></td>
        <td>{city['weather']}</td>
    </tr>

    <tr>
        <td><b>Temperature</b></td>
        <td>{city['temperature']} °C</td>
    </tr>

    <tr>
        <td><b>AQI</b></td>
        <td>{city['aqi']} ({city['air']})</td>
    </tr>

    <tr>
        <td><b>Traffic</b></td>
        <td>{city['traffic_status']}</td>
    </tr>

    <tr>
        <td><b>Parking</b></td>
        <td>{city['parking_status']}</td>
    </tr>

    <tr>
        <td><b>Electricity</b></td>
        <td>{city['electricity']} MW</td>
    </tr>

    </table>

    </div>
    """, unsafe_allow_html=True)

with summary2:

    score = city["city_score"]

    if score >= 90:
        color = "#22c55e"
        status = "Excellent"

    elif score >= 70:
        color = "#3b82f6"
        status = "Good"

    elif score >= 50:
        color = "#f59e0b"
        status = "Average"

    else:
        color = "#ef4444"
        status = "Critical"

    st.markdown(f"""
    <div class="info-card">

    <h3>⭐ Smart City Health</h3>

    <h1 style="
        text-align:center;
        font-size:60px;
        color:{color};
    ">
        {score}
    </h1>

    <h3 style="text-align:center;">
        {status}
    </h3>

    </div>
    """, unsafe_allow_html=True)

st.markdown("---")



st.markdown("## 🟢 Dashboard Status")

status_col1, status_col2, status_col3, status_col4 = st.columns(4)

with status_col1:
    st.success("✅ AI Engine Online")

with status_col2:
    st.success("✅ Live Monitoring")

with status_col3:
    st.success("✅ Charts Active")

with status_col4:
    st.success("✅ Data Updated")

st.markdown("---")



st.markdown("## 🤖 AI Smart Assistant")


question = st.text_input("Ask AI")

if question:

    answer = ask_ai(question, city)

    st.success(answer)

