import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import os

slider = st.select_slider('Decade', options=[1750,1760,1770,1780,1790,1800,1810,1820,1830,1840,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020])
st.write(f'Carbon Emissions by Country for the Year {slider}(billion tons of C)')
slider = '1700'

file1 = open('data/country_by_decade_emissions.csv', 'r')
file2 = open("data/temp_file.csv", 'a')

def fill_temp():
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
                ems = float(items[3]) / 1000
                loop = f'{ems},{items[4]},{items[5]}'
                print(loop)
                file2.write(loop)
            loop = ''
        checker = slider
        file2.close()
fill_temp()

real_data = pd.read_csv('data/temp_file.csv')
data = pd.DataFrame({
    "Emissions": real_data['Emissions'],
    "LAT": real_data['LAT'],
    "LON": real_data['LON']
})

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=data['LAT'].mean(),
        longitude=data['LON'].mean(),
        zoom=4,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ColumnLayer',
            data=data,
            get_position='[lon, lat]',
            radius=100000,
            elevation_scale=1,
            get_elevation_value=data['Emissions'],
            elevation_range=[0, 1000],
            extruded=True,
            pickable=True,
        ),
    ],
))
"""
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=data['lat'].mean(),
        longitude=data['lon'].mean(),
        zoom=4,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[lon, lat]',
            get_radius=100000,
            get_color=[255, 0, 0],  # red color
            pickable=True,
        ),
    ],
))"""