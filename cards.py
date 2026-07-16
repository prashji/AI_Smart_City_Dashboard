import streamlit as st

def premium_cards(city):

    weather_icon = {
        "Sunny": "☀️",
        "Cloudy": "☁️",
        "Rainy": "🌧️",
        "Night": "🌙"
    }

    c1, c2, c3, c4, c5 = st.columns(5)

    # Weather
    with c1:
        st.markdown(f"""
        <div class="premium-card">
            <div class="card-title">Weather</div>
            <div class="card-icon">{weather_icon.get(city["weather"], "🌤️")}</div>
            <div class="card-value">{city["temperature"]}°C</div>
            <div class="card-status">{city["weather"]}</div>
        </div>
        """, unsafe_allow_html=True)

    # AQI
    with c2:
        st.markdown(f"""
        <div class="premium-card red">
            <div class="card-title">AQI</div>
            <div class="card-icon">🌫️</div>
            <div class="card-value">{city["aqi"]}</div>
            <div class="card-status">{city["air"]}</div>
        </div>
        """, unsafe_allow_html=True)

    # Traffic
    with c3:
        st.markdown(f"""
        <div class="premium-card orange">
            <div class="card-title">Traffic</div>
            <div class="card-icon">🚗</div>
            <div class="card-value">{city["traffic"]}%</div>
            <div class="card-status">{city["traffic_status"]}</div>
        </div>
        """, unsafe_allow_html=True)

    # Electricity
    with c4:
        st.markdown(f"""
        <div class="premium-card blue">
            <div class="card-title">Electricity</div>
            <div class="card-icon">⚡</div>
            <div class="card-value">{city["electricity"]}</div>
            <div class="card-status">kWh</div>
        </div>
        """, unsafe_allow_html=True)

    # Parking
    with c5:
        st.markdown(f"""
        <div class="premium-card green">
            <div class="card-title">Parking</div>
            <div class="card-icon">🅿️</div>
            <div class="card-value">{city["parking"]}%</div>
            <div class="card-status">{city["parking_status"]}</div>
        </div>
        """, unsafe_allow_html=True)