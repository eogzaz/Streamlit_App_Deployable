import json
import streamlit as st
import pandas as pd
import requests
import streamlit_lottie as st_lottie

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
st.title(":blue[Pollution and Energy Overview II]")
st.header(' ',divider='grey')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(':grey[Part II:] :orange[Three Major Types of Pollution]')
st.write(' ')
st.write(' ')

# Section for Air Pollution
st.header(':red[Air Pollution]')

# Embedding video on pollution
if st.checkbox(':grey[Click to view video on air pollution.]'):
    st.video(data="https://www.youtube.com/embed/e6rglsLy1Ys?si=o9XRZy-HbTxPot8M")
    st.write(":grey[Video from National Geographic on YouTube.]")
st.header(' ',divider='red')
st.write('Air pollution is caused by the release of :red[pollutants] into the :green[atmosphere].')

# Loading animation for air pollution
st_lottie(load_lottie_file("animations/air.json"))

# Air pollution information
st.write('Sources of air pollution include :red[vehicle emissions], :red[industrial activities], :red[burning fossil fuels], and :red[large-scale agricultural practices].')
st.write('Pollutants can have :red[harmful effects] on :green[human health], including :red[respiratory issues], :red[cardiovascular diseases], and even :red[cancer].')
st.write('Air pollution also contributes to environmental problems like :red[acid rain], :red[ozone depletion], and :red[climate change].')
st.write(' ')
st.write(' ')

# Section for Water Pollution
st.header(':blue[Water Pollution]')

# Embedding video on pollution
if st.checkbox(':grey[Click to view video on water pollution.]'):
    st.video(data="https://youtu.be/4Q8dL8RtQM0?si=TsBJtbeCPlpKPkgL")
    st.write(":grey[Video from Next Generation Science on YouTube.]")
st.header(' ',divider='blue')
st.write('Water pollution occurs when :blue[contaminants] are discharged into bodies of water, such as :green[rivers], :green[lakes], :green[oceans], and :green[groundwater].')

# Loading animation for water pollution
st_lottie(load_lottie_file("animations/water.json"))

# Water pollution information
st.write('Sources of water pollution include :blue[industrial waste], :blue[agricultural runoff], :blue[sewage discharge], :blue[oil spills], and :blue[littering].')
st.write('Pollutants like :blue[heavy metals], :blue[pesticides], :blue[fertilizers], and :blue[plastics] can harm aquatic ecosystems, leading to the :blue[decline of fish populations], :blue[loss of biodiversity], and :blue[contamination of drinking water sources].')
st.write('Water pollution also poses :blue[health risks] to humans, causing diseases such as :blue[cholera], :blue[dysentery], and :blue[hepatitis], along with many others.')
st.write(' ')
st.write(' ')

# Section for Soil Pollution
st.header(':orange[Soil Pollution]')

# Embedding video on pollution
if st.checkbox(':grey[Click to view video on soil pollution.]'):
    st.video(data="https://youtu.be/wHcY-iFSYZM?si=nBAzx0nxfNAMiMxY")
    st.write(":grey[Video from Next Generation Science on YouTube.]")
st.header(' ',divider='orange')
st.write('Soil pollution refers to the presence of :orange[toxic chemicals], :orange[heavy metals], or other :orange[pollutants] in the :green[soil].')

# Loading animation for soil pollution
st_lottie(load_lottie_file("animations/soil.json"))

# Soil pollution information
st.write(':orange[Industrial activities], :orange[improper waste disposal], :orange[mining operations], and the use of :orange[pesticides and fertilizers] contribute to soil contamination.')
st.write('Contaminated soil can :orange[affect plant growth], :orange[reduce agricultural productivity], and :orange[pose risks to human health] through the consumption of :orange[contaminated food] or :orange[exposure to toxic substances].')
