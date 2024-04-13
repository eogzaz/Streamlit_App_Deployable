import json
import streamlit as st

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
st.title(":blue[Pollution and Energy Overview III]")
st.header(' ',divider='grey')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(':grey[Part III:] :orange[What IS Energy?]')

# Embedding video on energy
if st.checkbox(':grey[Click to view video on air energy basics.]'):
    st.video(data="https://youtu.be/CW0_S5YpYVo?si=E_tbMtRJmt3lRXdQ")
    st.write(":grey[Video from SciShow on YouTube.]")

# Renewable and Non-Renewable energy overview
st.header(' ',divider='grey')
st.write(':green[Energy] is a fundamental concept in physics and refers to the ability to work :green[work] or produce :green[change]. There are two major sources for energy that we know of; :green[renewable energy] and :red[non-renewable energy].')
st.write(':green[Renewable energy] is derived from natural resources that are :green[replenished] over time, such as :green[sunlight(]:grey[solar energy]:green[)], :green[wind(]:grey[wind turbines]:green[)], :green[water(]:grey[hydropower]:green[)], :green[biomass(]:grey[carbon-based organisms]:green[)], and :green[geothermal heat(]:grey[volcanoes & geothermal vents]:green[)].')
st.write(':red[Non-renewable energy] is derived from finite resources that are :red[not replenished] on a human timescale, including :red[fossil fuels(]:grey[coal, oil, natural gas]:red[)] and :red[nuclear energy(]:grey[from radioactive materials]:red[)].')
st.header(' ',divider='grey')

# Section for Kinetic Energy
st.write('The most basic forms that we see energy take place in our world are; :orange[kinetic energy(]:grey[energy of motion]:orange[)];')
st.video(data='https://youtu.be/c0KSjpPoNeQ?si=F-BJu3QW7Kwh9PKu')
st.write(':grey[Video from The Franklin Institute on YouTube.]')
st.write(":orange[Kinetic energy] is the energy possessed by an object due to its :orange[motion]. It is one of the fundamental forms of :orange[energy] and is directly related to the object's :orange[mass] and :orange[velocity]. We see :orange[kinetic energy] every single day from flying birds to speeding cars down a highway, :orange[kinetic] energy is everywhere.")
st.header(' ',divider='orange')
st.write(' ')
st.write(' ')

# Section for Potential Energy
st.write(':orange[potential energy(]:grey[stored energy]:orange[)];')
st.video('https://youtu.be/oeGUb9Rbts8?si=7t9z7sFcItDf0qnd')
st.write(':grey[Video from EarthPen on YouTube.]')
st.write(":orange[Potential energy] is the energy stored in an object due to its :orange[position] or :orange[configuration]. Unlike kinetic energy, which is associated with motion, :orange[potential energy] is associated with the :orange[potential] to do :orange[work] or cause a :orange[change].")
st.write("There are several types of potential energy, including :orange[gravitational] potential energy, :orange[elastic] potential energy, :orange[chemical] potential energy, and :orange[electrical] potential energy. Potential energy is a ")
st.header(' ',divider='orange')
st.write(' ')
st.write(' ')

# Section for Thermal Energy
st.write(':red[thermal energy(]:grey[heat]:red[)];')
st.video('https://youtu.be/9rmKtqpAt5I?si=F_DMYdXcDvE5EPs6&t=39')
st.write(':grey[Video from Next Generation Science on YouTube(skip to 40 seconds).]')
st.write(":red[Thermal energy], also known as heat energy, is the :red[energy] that comes from the vibrations and movements of :red[atoms] and :red[molecules] within a substance.")
st.write("It is a form of :red[kinetic energy] associated with the random :red[motion] of :red[particles] at the microscopic level, most commonly associated with :red[fire] as the most recognizeable form of this :red[energy]. Thermal energy determines the temperature of a substance and is transferred between objects through mechanisms such as :red[conduction], :red[convection], and :red[radiation].")
st.header(' ',divider='red')
st.write(' ')
st.write(' ')

# Section for Chemical Energy
st.write(':green[chemical energy(]:grey[energy stored in chemical bonds]:green[)];')
st.video('https://youtu.be/oQEJRhxw8VI?si=5QPeou85N2LC3hpe')
st.write(':grey[Video from Next Generation Science on YouTube.]')
st.write(":green[Chemical energy] is a form of :green[potential energy] stored within the :green[chemical bonds] of molecules. It is :green[released] or :green[absorbed] during :green[chemical reactions] when bonds are :green[broken] or :green[formed].")
st.write(":green[Chemical energy] is one of the most prevalent forms of :green[energy] and is essential for sustaining life and powering various :green[natural] and :green[technological] processes.")
st.header(' ',divider='green')
st.write(' ')
st.write(' ')

# Section for Electrical Energy
st.write(':orange[electrical energy(]:grey[energy associated with electric charges]:orange[)];')
st.video('https://youtu.be/ja8U4bFhEGQ?si=Pa9NUWk4BnWp2OoX')
st.write(':grey[Video from Next Generation Science on YouTube.]')
st.write(":orange[Electrical energy] is a form of :orange[energy] associated with the :orange[movement] of :orange[electric charges]. It is a type of :orange[kinetic energy] transferred through :orange[electrical circuits] and used to power various :orange[devices] and :orange[systems].")
st.write(":orange[Electrical energy] is generated from various sources and plays a crucial role in modern society for :orange[lighting], :orange[heating], :orange[transportation], :orange[communication], and :orange[industrial processes].")
st.header(' ',divider='orange')

# Section for Nuclear Energy
st.write('and :orange[nuclear energy(]:grey[energy created from nuclear reactions]:orange[)].')
st.write(":orange[Nuclear energy] is generated through :orange[nuclear reactions], such as :orange[fission] and :orange[fusion]. In :orange[nuclear fission], heavy atomic nuclei :orange[split] into smaller nuclei, releasing large amounts of :orange[energy]. :orange[Nuclear fusion], on the other hand, involves :orange[combining] light atomic nuclei to form heavier nuclei, releasing even more :orange[energy].")
st.video('https://youtu.be/44ovdxOvP_A?si=VOwJbesHSM3iDlE6')
st.write(':grey[Video from Student Energy on YouTube]')
st.write("Although :orange[nuclear energy] is not technically a :orange[non-renewable] source of :orange[energy], and it is not exactly a :orange[renewable] source either, it is instead termed an :green[alternative energy source] and a lot of energy in :orange[nuclear reactions] is lost due to heat dissipation. Even though it may not be the most :orange[environmentally] friendly or even harmful, :orange[nuclear energy] proves to be a reliable source of large amounts of energy, making it a good power source for large cities or industrialized areas.")
st.header(' ',divider='orange')

# Embedding video on energy
if st.checkbox(':grey[Click to view aditional videos on energy.]'):
    st.video(data='https://youtu.be/rkZZjM6Oiw8?si=Yoqt04FnZC82-9bV')
    st.write(':grey[Video from Next Generation Science on YouTube.]')
    st.video(data="https://youtu.be/FX7T-QYTPho?si=SC_0ljtK--eldkEC")
    st.write(":grey[Video from MooMooMath and Science on YouTube.]")
st.header(' ',divider='grey')