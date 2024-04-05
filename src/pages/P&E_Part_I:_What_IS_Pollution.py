import json
import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# Creating sidebar message to prompting user to choose a directory
st.sidebar.success("Choose a page from directory above.")

# Function to load Lottie File animations
def load_lottie_file(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

# Linking all of the pages at the top of the page
st.page_link('Main_Page.py', label="Home Page")
st.page_link('pages/Emissions_By_Decade.py', label="Page 1: Emissions by Decade")
st.page_link('pages/P&E_Part_I:_What_IS_Pollution.py', label="Page 2: P&E 1 - What is Pollution")
st.page_link('pages/P&E_Part_II:_Three_Major_Types_Pollution.py', label="Page 3: P&E 2 - Three Types of Pollution")
st.page_link('pages/P&E_Part_III:_What_IS_Energy.py', label="Page 4: P&E 3 - What is Energy")
st.page_link('pages/P&E_Part_IV:_Energy_Creation,_Storage,_&_Transfer.py', label="Page 5: P&E 4 - Energy Creation, Storage & Transfer")
st.page_link('pages/P&E_Part_V:_Renewable_Energy.py', label="Page 6: P&E 5 - Renewable Energy")

# Page title and subtitle, with spacing and dividers
st.header(' ',divider='grey')
st.title(":blue[Pollution and Energy Overview I]")
st.header(' ',divider='grey')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(':grey[Part I:] :orange[What IS Pollution?]')
st.write(' ')

# Embedding video on pollution
if st.checkbox(':grey[Click to view video on a brief history of carbon emissions.]'):
    st.video(data="https://youtu.be/EQ7S0D1iucY?si=V5bb3vBTS-OzEGPZ")
    st.write(":grey[Video from Potsdam Institute for Climate Impact Research PIK on YouTube.]")
st.header(' ',divider='grey')

# Information on pollution, what forms it comes in, and the effects that it has on the world
st.write(":red[Pollution] occurs when harmful substances are introduced into the :green[environment], causing adverse effects on :green[living organisms] and :green[ecosystems]. There are many forms of :red[pollution], and many different ways that these :red[pollutants] can be formed from natural processes to human industrialization.")

# Loading animation of nature dying
st_lottie(load_lottie_file("animations/killing_nature.json"))
st.write(":red[Pollution] not only causes :red[respiratory harm] to :green[humans] and :green[animals], but also causes the :green[climate] to warm, :red[changing] entire :green[ecosystems] of a region. If the issues persist, a lot of the :red[changes] that come to the world will be irreversible, causing more domino effects of world degredation.")

# Divider
st.subheader(' ', divider='grey')

st.write("These :red[pollutants] can be in the form of :green[solid], :green[liquid], or :green[gas], and they often result from human activities such as :red[industrial processes], :red[transportation], :red[agriculture], and :red[waste disposal].")

# Loading animation of industrial plant
st_lottie(load_lottie_file("animations/emissions.json"))
st.write(":red[Pollutants] are harmful substances released into the :green[environment] that can have severe effects on :green[ecosystems], :green[wildlife], and :green[human health]. They form through various natural and human activities, contributing to :red[air], :red[water], and :red[soil pollution].")

# Divider
st.header(' ',divider='grey')

st.write("Some common pollutants include :red[carbon dioxide (]:grey[CO2]:red[)], :red[sulfur dioxide (]:grey[SO2]:red[)], :red[nitrogen dioxide (]:grey[NO2]:red[)], :red[particulate matter (]:grey[PM]:red[)], :red[ozone (]:grey[O3]:red[)], :red[heavy metals], and various :red[chemical compounds].")

# Loading animation of the world
st_lottie(load_lottie_file("animations/climate_change.json"))

st.write(":red[Pollution] is extremely harmful to the :green[environment], and everything that lives in it. From the :red[disease] that comes with breathing in the :red[polluted air] to the broader term of :red[climate change], pollution has extreme adverse effects on the :green[ecosystem], and ramififcations must be made before the changes become :red[irreversible].")
st.header(' ',divider='grey')

# Embedding videos on pollution with a checkbox feature
if st.checkbox(':grey[Click to view additional videos regarding pollution/climate change.]'):
    st.video(data="https://youtu.be/G4H1N_yXBiA?si=KIV9IYQ5ltZPfUuB")
    st.write(":grey[Video from National Geographic on YouTube.]")
    st.header(' ',divider='grey')
    st.video(data="https://youtu.be/_6xlNyWPpB8?si=tIvJcGNNPHETgiI_")
    st.write(":grey[Video from TED-Ed on YouTube.]")
    st.header(' ',divider='grey')
    st.video(data="https://youtu.be/ipVxxxqwBQw?si=0QJBNYwFRcujoIJU")
    st.write(":grey[Video from Kurzgesagt on YouTube.]")
st.header(' ',divider='grey')
