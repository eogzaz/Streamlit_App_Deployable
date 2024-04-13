import json
import streamlit as st
from streamlit_lottie import st_lottie

# Function to load animations 
def load_lottie_file(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

st.sidebar.success("Choose a page from directory above.")

# Linking all of the pages at the top of the page
st.page_link('Main_Page.py', label="Home Page")
st.page_link('pages/Emissions_By_Decade.py', label="Page 1: Emissions by Decade")
st.page_link('pages/P&E_Part_I:_What_IS_Pollution.py', label="Page 2: P&E 1 - What is Pollution")
st.page_link('pages/P&E_Part_II:_Three_Major_Types_Pollution.py', label="Page 3: P&E 2 - Three Types of Pollution")
st.page_link('pages/P&E_Part_III:_What_IS_Energy.py', label="Page 4: P&E 3 - What is Energy")
st.page_link('pages/P&E_Part_IV:_Energy_Creation,_Storage,_&_Transfer.py', label="Page 5: P&E 4 - Energy Creation, Storage & Transfer")
st.page_link('pages/P&E_Part_V:_Renewable_Energy.py', label="Page 6: P&E 5 - Renewable Energy")

# Creating Main Page Title and adding the checkbox where videos on climate change are embeddee
st.header(' ',divider='grey')
st.title(':blue[The Global Pollution-Energy Index:]')
st.header(':blue[Global Pollution Visualized]')
if st.checkbox(":grey[Click to view videos on climate change and WHY we need change.]"):
    st.video(data='https://youtu.be/jAa58N4Jlos?si=S_wLMd6HmNN10QHW')
    st.write(":grey[Video from National Geographic on YouTube.]")
    st.video(data='https://youtu.be/uFlLDcppwpI?si=UuDe80CmGOiNR4LD')
    st.write(':[Video from The Telegraph on YouTube.]')
st.header(' ',divider='grey')
st.write(' ')
st.write(' ')

st.write('This in-depth website articulates the framework for a significant change in :red[human activity] overall, not only encompassing the central concept but also laying out the extensive :green[groundwork], :green[motivation], and :green[ideas] indispensable for its execution. This undertaking is propelled by a genuine motivation—to bridge the gaps in understanding :red[global emissions] and :orange[energy consumption], and to help the future of our :green[environment].')

with open("animations/energy.json", "r") as f:
    data = json.load(f)
st_lottie(data)

st.write('Those unfamiliar or just beginning to embark on the understanding of how :orange[energy] is :green[created], :green[transferred], and especially on how it :red[pollutes] would find this document as a perfect place to start learning. The overarching aim is to :green[cultivate awareness], rendering the broader population well-informed in the critical issues of our time. Specifically, my project endeavors to illuminate the significance of :green[renewable energy] for our collective future, in order to protect the environment against further :red[degradation]. This information will be arranged in a way that is engaging for users and that has the capacity to educate those who will be most affected by the :red[consequences] of :red[global emissions] and :red[climate change].')
st.header(' ',divider='grey')
st.write(' ')

st.write('To actualize this educational initiative this interactive website is a user-centric platform designed to provide intuitive insights into :orange[energy use] and its ramifications on the environment, specifically :red[pollution]. At the core of this initiative lies a series of interactive maps, serving as an engaging interface to provide information about :orange[energy consumption], :red[pollution], and other :green[important data] or :green[literature] that is relevant to the argument. Powered by straightforward charts, graphs, and maps the website seeks to communicate its messages in a comprehensible and accessible manner.')

with open("animations/learning.json", "r") as f:
    data = json.load(f)
st_lottie(data)

st.write('The backbone of this project rests on :green[data] and :green[functionality] primarily, incorporating multiple maps containing various :green[data sets] that users can interact with seamlessly. Whether through hovering over or clicking on specific regions, users can unearth detailed information, encompassing data sources and other insightful perspectives. The primary focus remains on presenting information about :red[pollutants], :red[carbon emissions], and the different types of :orange[energy use] in a given area. This will give users a much more rounded understanding of how their community operates in terms of :orange[energy usage], and also to see how much :red[pollution] is constantly being pumped into their air.')
st.header(' ',divider='grey')
st.write(' ')

st.write('This project also confronts a prevalent challenge -— the :red[lack of comprehension] surrounding the technologies ingrained in our daily lives. This interactive website stands as an :green[educational aid], unraveling the intricacies of these devices and :green[enhancing understanding] of their :red[environmental implications]. This project aligns with the imperative to debunk :red[misinformation] and dispel :red[false theories] circulating around :red[emissions] and :orange[energy]. In the wake of a significant shift towards :green[renewable energy], widespread awareness is of utmost importance, calling for a collective effort for change that spans across America, or preferably the world.')

with open("animations/teamwork.json", "r") as f:
    data = json.load(f)
st_lottie(data)

st.write('In a world undergoing profound changes influenced by :red[human activity], the project emerges as a plea for :green[collective action]. Acknowledging that :red[climate change] is a natural phenomenon, recognizing the :red[impact] of human activities, and taking :green[proactive measures] are the three steps most important for the pivotal switch for humanity. The inevitable :red[depletion of natural gas and coal] amplifies the urgency of transitioning to :green[renewable energies] before our resources are :red[depleted].')
st.header(' ',divider='grey')
st.write(' ')

st.write('The narrative embraces the understanding that monumental shifts happen :green[incrementally]. Every small stride towards :green[acknowledging] and :green[addressing] the crisis contributes to the larger goal. Whether or not humans are the direct cause of climate change is meaningless in the face of the real :red[impacts of climate change] today, we must act on these to mitigate further change that could possibly be :red[irreversible].')

with open("animations/climb.json", "r") as f:
    data = json.load(f)
st_lottie(data)

st.write('In essence, this project is persistent in that understanding ones direct impact on the :green[environment] propels humanity towards a :green[sustainable] future. Closing the :red[knowledge gap] surrounding :red[emissions] and :orange[energy use] stands as the foreground for creating a :green[safer and healthier Earth] for future civilizations to thrive. The start towards a better world begins with :green[shared knowledge] and :green[collective action].')
if st.checkbox(":grey[Click to view another video on climate change.]"):
    st.video('https://youtu.be/-n4A0BssFd0?si=em97RXyPmX6M4laa')
    st.write(":grey[Video from Climate-KIC on YouTube.]")
st.header(' ',divider='grey')