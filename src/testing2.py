import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

maps = pd.read_csv('data/country_by_decade_emissions.csv')
map_data = pd.DataFrame({
    "Emissions": maps['Emissions'],
    "LAT": maps['LAT'],
    "LON": maps['LON'],
    "Year": maps['Year']
})
st.write(map_data)
#map_data = pd.DataFrame(map_data)

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk,
        pdk.Layer(
           'HexagonLayer',
           data=map_data,
           get_position='[LAT, LON]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=map_data,
            get_position='[LAT, LON]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

"""
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])
st.write(chart_data)
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk,
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
"""
def doesitfuckingmatter():
    checker = '1750'
    emissions_max = 0
    if checker != slider:
        os.remove('data/temp_file.csv')
        file2 = open("data/temp_file.csv", 'a')
        count = 0
        for my_data in file1:
            loop = ''
            items = my_data.split(',')
            if count == 0:
                headers = f'{items[3]},{items[4]},{items[5]}'
                file2.write(headers)
            count += 1
            if items[2] == str(slider):
                if float(items[3]) > emissions_max:
                    emissions_max = float(items[3])
                ems = float(items[3])# / 1000
                loop = f'{ems},{items[4]},{items[5]}'
                print(loop)
                file2.write(loop)
            loop = ''
        checker = slider
        file2.close()
        temp_data = pd.read_csv('data/temp_file.csv')
        map_data = pd.DataFrame({
            "Emissions": temp_data['Emissions'],
            "LAT": temp_data['LAT'],
            "LON": temp_data['LON']
        })