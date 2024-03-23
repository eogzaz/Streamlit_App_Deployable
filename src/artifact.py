import streamlit as st
import pandas as pd
import numpy as np
import os
import pydeck as pdk

DATE_COLUMN = 'date/time'

data_load_state = st.text('Loading data...')
total_data = pd.read_csv('data/total_emissions_global_2019.csv', dtype={"Year": str}, nrows=223)
capita_data = pd.read_csv('data/emissions_per_capita_2019.csv', dtype={"Year": str}, nrows=223)
global_data = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str}, nrows=270)
data_load_state.text("Done loading data! (using st.cache_data)")

if st.checkbox('Show raw data for total CO2 emissions from fossil fuels'):
    st.subheader('Raw data(thousand metric tons of C)')
    st.write(total_data)

if st.button('Show raw data for total global C02 emissions per capita'):
    st.subheader('Raw data(metric tons of C)')
    st.write(capita_data)

if st.toggle('Show raw data for total global C02 emissions from 1751-2019'):
    st.subheader('Raw data(million metric tons of C)')
    st.write(global_data)

st.subheader('Line chart of global emissions from 1751 to 2019(metric tons of C).')
if st.checkbox('Global Carbon Emissions by fossil fuel(Line Chart)'):
    df = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str})
    chart_data = pd.DataFrame(df, columns=["Year", "Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    st.line_chart(chart_data, x="Year", y=["Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])

st.subheader('Bar chart of global emissions from 1751 to 2019(metric tons of C).')
if st.checkbox('Global Carbon Emissions by fossil fuel(Bar Chart)'):
    df = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str})
    chart_data = pd.DataFrame(df, columns=["Year", "Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    st.bar_chart(chart_data, x="Year", y=["Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])

st.subheader('Area chart of global emissions from 1751 to 2019(metric tons of C).')
if st.checkbox('Global Carbon Emissions by fossil fuel(Area Chart)'):
    df = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str})
    chart_data = pd.DataFrame(df, columns=["Year", "Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    st.area_chart(chart_data, x="Year", y=["Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])

st.subheader('Map of total global emissions in 2019.')
if st.checkbox('Show map of global carbon emissions(thousand metric tons of C)'):
    df = pd.read_csv('data/total_emissions_global_2019.csv')
    chart_data = pd.DataFrame(df, columns=['Emissions', 'LAT', 'LON'])
    st.map(chart_data, size='Emissions')

st.subheader('Map of Country Carbon Emissions by Decade')
checker = '1750'
slider = st.select_slider('Decade', options=[1750,1760,1770,1780,1790,1800,1810,1820,1830,1840,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020])
st.write(f'Carbon Emissions by Country for the Year {slider}(billion tons of C)')

file1 = open('data/country_by_decade_emissions.csv', 'r')
#file2 = open("data/temp_file.csv", 'a')

@st.cache_data
def make_map(map_data):
    st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=4,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=map_data,
            get_position='[lon, lat]',
            radius=100000,
            elevation_scale=1,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
))
if slider == 1750:
    temp_data = pd.read_csv('data/emissions_1750.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'],
        "lat": temp_data['LAT'],
        "lon": temp_data['LON']
    })
    make_map(map_data)
elif slider == 1760:
    temp_data = pd.read_csv('data/emissions_1760.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'],
        "lat": temp_data['LAT'],
        "lon": temp_data['LON']
    })
    make_map(map_data)
elif slider == 1770:
    temp_data = pd.read_csv('data/emissions_2020.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'],
        "lat": temp_data['LAT'],
        "lon": temp_data['LON']
    })
    make_map(map_data)
elif slider == 1780:
    temp_data = pd.read_csv('data/emissions_1780.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'],
        "lat": temp_data['LAT'],
        "lon": temp_data['LON']
    })
    make_map(map_data)
elif slider == 1790:
    temp_data = pd.read_csv('data/emissions_1760.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'],
        "lat": temp_data['LAT'],
        "lon": temp_data['LON']
    })
    make_map(map_data)
elif slider == 1800:
    temp_data = pd.read_csv('data/emissions_1800.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'],
        "lat": temp_data['LAT'],
        "lon": temp_data['LON']
    })
    make_map(map_data)