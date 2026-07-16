import folium
from streamlit_folium import st_folium


def live_city_map(city_name, lat, lon):

    m = folium.Map(

        location=[lat, lon],

        zoom_start=12,

        control_scale=True

    )

    folium.Marker(

        [lat, lon],

        popup=f"{city_name}",

        tooltip=city_name,

        icon=folium.Icon(

            color="red",

            icon="info-sign"

        )

    ).add_to(m)

    st_folium(

        m,

        width=None,

        height=500,

        returned_objects=[]

    )