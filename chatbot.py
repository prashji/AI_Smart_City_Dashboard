import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_ai(question, city):
    
    prompt = f"""
You are the AI Assistant for the AI Smart City Dashboard.

Your job is to help users understand THIS dashboard.

Current Dashboard Data:
- City: {city_name if 'city_name' in locals() else 'Selected City'}
- Weather: {city['weather']}
- Temperature: {city['temperature']}°C
- AQI: {city['aqi']}
- Traffic: {city['traffic']}%
- Parking: {city['parking']}%
- Electricity: {city['electricity']}
- Smart City Score: {city['city_score']}

You should answer:
✅ What is AQI?
✅ Explain AQI shown in the dashboard.
✅ What does Traffic mean?
✅ Explain Parking.
✅ Explain Smart City Score.
✅ Explain Electricity usage.
✅ Explain charts.
✅ Explain dashboard features.
✅ Give suggestions based on current dashboard values.

If the user asks about any topic unrelated to the dashboard (movies, cricket, history, coding, celebrities, etc.), reply exactly:

"I can only help with this AI Smart City Dashboard."

User Question:
{question}
"""

    response = model.generate_content(prompt)
    return response.text