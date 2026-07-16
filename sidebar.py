import streamlit as st

from utils.config import (
    APP_NAME,
    CITY_LIST,
    WEATHER_OPTIONS,
    DEFAULT_TEMP,
    DEFAULT_AQI,
    DEFAULT_TRAFFIC,
    DEFAULT_ELECTRICITY,
    DEFAULT_PARKING,
    MIN_TEMP,
    MAX_TEMP,
    MIN_AQI,
    MAX_AQI,
    MIN_TRAFFIC,
    MAX_TRAFFIC,
    MIN_ELECTRICITY,
    MAX_ELECTRICITY,
    MIN_PARKING,
    MAX_PARKING,
)


def premium_sidebar():

    with st.sidebar:

        st.image("images/logo.png", width=90)

        st.markdown(f"# 🌍 {APP_NAME}")

        st.caption("AI Powered Smart City Monitoring")

        st.markdown("---")

        city = st.selectbox(
            "🏙 Select City",
            CITY_LIST
        )

        weather = st.selectbox(
            "🌤 Weather",
            WEATHER_OPTIONS
        )

        st.markdown("---")

        st.subheader("🌡 Environment")

        temperature = st.slider(
            "Temperature (°C)",
            MIN_TEMP,
            MAX_TEMP,
            DEFAULT_TEMP
        )

        aqi = st.slider(
            "AQI",
            MIN_AQI,
            MAX_AQI,
            DEFAULT_AQI
        )

        st.markdown("---")

        st.subheader("🚦 Smart Utilities")

        traffic = st.slider(
            "Traffic %",
            MIN_TRAFFIC,
            MAX_TRAFFIC,
            DEFAULT_TRAFFIC
        )

        electricity = st.slider(
            "Electricity (MW)",
            MIN_ELECTRICITY,
            MAX_ELECTRICITY,
            DEFAULT_ELECTRICITY
        )

        parking = st.slider(
            "Parking %",
            MIN_PARKING,
            MAX_PARKING,
            DEFAULT_PARKING
        )

        st.markdown("---")

        st.subheader("🟢 System Status")

        st.success("Weather API : Ready")

        st.success("AQI Engine : Ready")

        st.success("AI Module : Active")

        st.success("Dashboard : Online")

        st.markdown("---")

        st.caption("Version 3.0")

    return (
        city,
        weather,
        temperature,
        aqi,
        traffic,
        electricity,
        parking
    )