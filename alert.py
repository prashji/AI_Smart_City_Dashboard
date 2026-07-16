import streamlit as st

def city_alert(city):

    if city["aqi"]>150:

        st.error("🚨 Air Quality is Dangerous")

    if city["traffic"]>70:

        st.warning("🚦 Heavy Traffic")

    if city["temperature"]>40:

        st.warning("🌡 Heat Wave")

    if city["parking"]<20:

        st.error("🅿 Parking Full")