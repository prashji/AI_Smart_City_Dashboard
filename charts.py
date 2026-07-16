import plotly.graph_objects as go


# ==========================================
# TRAFFIC GAUGE CHART
# ==========================================

def traffic_chart(value):

    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=value,
            number={
                "suffix": "%",
                "font": {"size": 34, "color": "white"}
            },
            title={
                "text": "🚦 Traffic Density",
                "font": {"size": 20}
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1,
                    "tickcolor": "white"
                },
                "bar": {
                    "color": "#2563eb",
                    "thickness": 0.35
                },
                "bgcolor": "rgba(0,0,0,0)",
                "borderwidth": 2,
                "bordercolor": "#444",
                "steps": [
                    {"range": [0, 40], "color": "#16a34a"},
                    {"range": [40, 70], "color": "#facc15"},
                    {"range": [70, 100], "color": "#dc2626"},
                ],
            },
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=340,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    return fig


import plotly.graph_objects as go

def traffic_trend_chart():

    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    traffic = [45,60,48,72,58,80,62]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=days,
            y=traffic,
            mode="lines+markers",
            line=dict(width=4, color="#4ade80"),
            marker=dict(size=8),
            fill="tozeroy"
        )
    )

    fig.update_layout(
        title="🚦 Traffic Flow (This Week)",
        template="plotly_dark",
        height=300,
        margin=dict(l=10,r=10,t=40,b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="",
        yaxis_title=""
    )

    return fig


# ==========================================
# AQI BAR CHART
# ==========================================

def pollution_chart(aqi):

    if aqi <= 50:
        color = "#16a34a"
    elif aqi <= 100:
        color = "#facc15"
    elif aqi <= 150:
        color = "#fb923c"
    else:
        color = "#dc2626"

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=["AQI"],
            y=[aqi],
            text=[aqi],
            textposition="outside",
            marker=dict(
                color=color,
                line=dict(color="white", width=1)
            ),
            width=[0.5]
        )
    )

    fig.update_layout(
        title="🌫 Air Quality Index",
        template="plotly_dark",
        height=340,
        yaxis=dict(range=[0, 300]),
        xaxis=dict(showgrid=False),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=20),
        font=dict(color="white")
    )

    return fig

def aqi_trend_chart():
    
    days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    aqi=[90,120,160,130,170,140,150]

    fig=go.Figure()

    fig.add_trace(

        go.Bar(

            x=days,

            y=aqi,

            marker_color="#84cc16"

        )

    )

    fig.update_layout(

        title="🌫 AQI Trend (This Week)",

        template="plotly_dark",

        height=300,

        margin=dict(l=10,r=10,t=40,b=10),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        xaxis_title="",

        yaxis_title=""

    )

    return fig

# ==========================================
# ELECTRICITY GAUGE
# ==========================================

def electricity_chart(value):

    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=value,
            number={"suffix": " MW"},
            title={"text": "⚡ Electricity"},
            gauge={
                "axis": {"range": [100, 600]},
                "bar": {"color": "#06b6d4"},
                "steps": [
                    {"range": [100, 250], "color": "#16a34a"},
                    {"range": [250, 450], "color": "#facc15"},
                    {"range": [450, 600], "color": "#dc2626"},
                ],
            },
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=340,
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


# ==========================================
# PARKING DONUT CHART
# ==========================================

def parking_chart(value):

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[value, 100 - value],
            labels=["Available", "Occupied"],
            hole=0.70,
            marker=dict(
                colors=["#16a34a", "#1e293b"]
            ),
            textinfo="percent"
        )
    )

    fig.update_layout(
        title="🅿 Parking Availability",
        template="plotly_dark",
        height=340,
        showlegend=True,
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


# ==========================================
# TEMPERATURE GAUGE
# ==========================================

def temperature_chart(temp):

    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=temp,
            number={"suffix": "°C"},
            title={"text": "🌡 Temperature"},
            gauge={
                "axis": {"range": [0, 50]},
                "bar": {"color": "#f97316"},
                "steps": [
                    {"range": [0, 20], "color": "#38bdf8"},
                    {"range": [20, 35], "color": "#16a34a"},
                    {"range": [35, 50], "color": "#dc2626"},
                ],
            },
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=340,
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig