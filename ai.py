# ==========================================
# utils/ai.py
# ==========================================

def get_ai_recommendation(city):
    """
    Generate AI recommendations based on city conditions.
    """

    recommendations = []

    # ======================================
    # AIR QUALITY
    # ======================================

    if city["aqi"] <= 50:
        recommendations.append(
            "✅ Air quality is excellent. Outdoor activities are recommended."
        )

    elif city["aqi"] <= 100:
        recommendations.append(
            "⚠ Air quality is moderate. Sensitive people should take precautions."
        )

    elif city["aqi"] <= 150:
        recommendations.append(
            "🟠 Air quality is unhealthy. Reduce prolonged outdoor exposure."
        )

    else:
        recommendations.append(
            "🔴 Air pollution is very high. Avoid outdoor activities and wear a mask."
        )

    # ======================================
    # TRAFFIC
    # ======================================

    if city["traffic"] <= 30:
        recommendations.append(
            "✅ Traffic flow is smooth across the city."
        )

    elif city["traffic"] <= 70:
        recommendations.append(
            "🚦 Moderate traffic detected. Consider alternate routes during peak hours."
        )

    else:
        recommendations.append(
            "🚗 Heavy traffic detected. Public transport is recommended."
        )

    # ======================================
    # PARKING
    # ======================================

    if city["parking"] >= 70:
        recommendations.append(
            "🅿 Parking spaces are widely available."
        )

    elif city["parking"] >= 30:
        recommendations.append(
            "🅿 Parking availability is limited."
        )

    else:
        recommendations.append(
            "❌ Parking is almost full. Use nearby parking facilities."
        )

    # ======================================
    # ELECTRICITY
    # ======================================

    if city["electricity"] >= 500:
        recommendations.append(
            "⚡ Electricity consumption is high. Energy-saving measures are recommended."
        )

    elif city["electricity"] >= 300:
        recommendations.append(
            "⚡ Electricity usage is within the normal operating range."
        )

    else:
        recommendations.append(
            "✅ Electricity demand is low and stable."
        )

    # ======================================
    # TEMPERATURE
    # ======================================

    temp = city["temperature"]

    if temp >= 40:
        recommendations.append(
            "🌡 Extreme heat detected. Stay hydrated and avoid direct sunlight."
        )

    elif temp <= 15:
        recommendations.append(
            "🥶 Low temperature detected. Wear warm clothing."
        )

    else:
        recommendations.append(
            "🌤 Temperature is comfortable."
        )

    # ======================================
    # WEATHER
    # ======================================

    weather = city["weather"]

    if weather == "Rainy":
        recommendations.append(
            "🌧 Roads may be slippery. Drive carefully."
        )

    elif weather == "Sunny":
        recommendations.append(
            "☀ Clear weather. Good conditions for travel."
        )

    elif weather == "Cloudy":
        recommendations.append(
            "☁ Cloudy conditions expected throughout the day."
        )

    elif weather == "Night":
        recommendations.append(
            "🌙 Night mode active. Ensure proper street lighting."
        )

    # ======================================
    # SMART CITY SCORE
    # ======================================

    score = city.get("city_score", 80)

    if score >= 90:
        recommendations.append(
            "🏆 Overall Smart City Health: Excellent."
        )

    elif score >= 70:
        recommendations.append(
            "✅ Overall Smart City Health: Good."
        )

    elif score >= 50:
        recommendations.append(
            "⚠ Overall Smart City Health: Average. Improvements are recommended."
        )

    else:
        recommendations.append(
            "🚨 Overall Smart City Health: Critical. Immediate action is required."
        )

    return recommendations