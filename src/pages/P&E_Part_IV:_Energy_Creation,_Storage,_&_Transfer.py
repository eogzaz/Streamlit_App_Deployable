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
st.title(":blue[Pollution and Energy Overview IV]")
st.header(' ',divider='grey')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(':grey[Part IV:] :orange[How is Energy Created, Stored, and Transferred?]')
st.write(' ')
st.write(' ')

if st.checkbox(":grey[Click to view video on how energy works in our daily lives.]"):
    st.video('https://youtu.be/rzsejNlvA8Y?si=ONpQC4V3v9C6hTxK')
    st.write(':grey[Video from  on YouTube]')
st.header(' ',divider='grey')

# Basic energy info to setup the following page
st.write(":blue[How is energy created?]")
st.write(":orange[Energy] cannot be :blue[created] or :blue[destroyed], only :green[converted] between different forms, so there is no real way to 'make' :orange[energy]. However, being able to convert :orange[energy] into different forms proves to be very useful to our technology today, and there are many ways that it can be :blue[converted].")
st_lottie(load_lottie_file('animations/battery.json'))
st.write("The different ways that we can convert :orange[energy] from one form to another are: :blue[chemical reactions], :blue[nuclear reactions], :blue[mechanical processes], :blue[thermal processes], :blue[geothermal energy], and :blue[renewable resources]. Each method has its advantages, limitations, and environmental impacts, highlighting the importance of adopting diverse and sustainable energy sources to meet global energy needs.")

if st.checkbox(":grey[Click to view video on energy generation.]"):
    st.video(data='https://youtu.be/0PpO-2mEO_0?si=BbXspXpczIChe647')
    st.write(':grey[Video from Student Energy on YouTube]')

st.header(' ',divider='grey')
st.write(' ')
st.write(' ')

st.write(":blue[How is energy stored?]")
st.write("The most common type of storage for :orange[energy] we know of today are :blue[batteries] and :blue[fuel cells]. Batteries are in essentially every piece technology we use, and they store their energy with chemicals such as :blue[lithium] that are able to release :orange[electrical energy] on command.")
st_lottie(load_lottie_file('animations/powercell.json'))
st.write("There are many other ways that :orange[energy] can be stored, using different energy types or materials altogether, but for the day-to-day lives that we live, :blue[batteries] are by far the most practical. There are other ways of storage that are mainly used in industrial processes such as: :blue[mechanical energy storage], :blue[electromagnetic energy storage], :blue[thermal energy storage], :blue[potential energy storage].")
st.write("These are some of the common ways in which :orange[energy] can be :blue[stored] for various applications, including :blue[grid stabilization], :blue[renewable energy integration], :blue[transportation], and :blue[industrial processes]. Each storage method has its advantages, limitations, and suitability for specific applications and :orange[energy systems].")

if st.checkbox(":grey[lick to view video on energy storage.]"):
    st.video(data='https://youtu.be/9eAFEU7pMwU?si=QAP8asWn_6aB0Dh4')
    st.write(':grey[Video from Student Energy on YouTube]')
st.header(' ',divider='grey')

st.write(":blue[How is energy transferred?]")
st.write(':orange[Energy] can be :green[transferred] from one source to another through various mechanisms, depending on the type of :orange[energy] and the :green[systems] involved.')
st_lottie(load_lottie_file('animations/plug.json'))
st.write('One of the ways that :orange[energy] can be :green[transferred] from one source to another is through :green[mechanical energy transfer], which is found mainly in transmission systems that consists of :green[gears], :green[pulleys], :green[belts], or :green[shafts], much like you would find in the engine bay of a car.')
st.write('Another way that :orange[energy] is :green[transferred] is through :green[electromagnetic energy transfer], and it comes in the form of :green[light], :green[radio waves], :green[microwaves], or :green[infrared light]. A way that we see this happen in everyday life is when :green[receivers] send out signals to antenna with :green[electromagnetic waves], and they get absorbed by the antenna.')
st_lottie(load_lottie_file('animations/transfer.json'))
st.write(':green[Thermal energy transfer] is one way of transferring :orange[energy] that we are likely all familiar with, whether for reasons good or bad. :green[Thermal energy] gets :green[transferred] through direct or indirect contact from what is usually :green[fire] to another source, like sitting around a campfire to stay warm and then roasting marshmallows in that campfire.')
st.write(':green[Electrical energy transferring] is one of the most important ways that we know how to transfer :orange[energy], because it is used so frequently by the entire world. :green[Electrical charges] flow through :green[cords] and :green[wires] that deliver :green[electricity] for your needs, typically seen as :green[chargers] or :green[power cords] for devices.')
st.write('The final way we transfer :orange[energy], arguably the most important for human life, is the process of :green[transferring chemical energy]. When bonds of :green[molecule]s are broken, it releases an enormous amount of :orange[energy] that can usually be harnessed by the heat it gives off. However, humans also use the process of :green[transferring chemical energ]y when we eat and digest food.')

st.header(' ',divider='grey')
if st.checkbox(":grey[Click to view additional videos on energy creation, storage, and transfer]"):
    st.video('https://youtu.be/-njmj0diWu8?si=pydUYr4M0jfcwwjr')
    st.write(':grey[Video from Student Energy on YouTube.]')
    st.header(' ',divider='grey')
    st.video('https://youtu.be/zaXBVYr9Ij0?si=vyLA97qNz-xXypym')
    st.write(':grey[Video from Student Energy on Youtube.]')
    st.header(' ',divider='grey')
    st.video('https://youtu.be/nbPmsBmo03Y?si=StRxEgqZ9lyF3RUa')
    st.write(':grey[Video from Engineering World on YouTube.]')
st.header(' ',divider='grey')
