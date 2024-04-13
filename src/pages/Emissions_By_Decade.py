import streamlit as st
import pandas as pd

# Creating sidebar message to prompting user to choose a directory
st.sidebar.success("Choose a page from directory above.")

# Linking all of the pages at the top of the page
st.page_link('Main_Page.py', label="Home Page")
st.page_link('pages/Emissions_By_Decade.py', label="Page 1: Emissions by Decade")
st.page_link('pages/P&E_Part_I:_What_IS_Pollution.py', label="Page 2: P&E 1 - What is Pollution")
st.page_link('pages/P&E_Part_II:_Three_Major_Types_Pollution.py', label="Page 3: P&E 2 - Three Types of Pollution")
st.page_link('pages/P&E_Part_III:_What_IS_Energy.py', label="Page 4: P&E 3 - What is Energy")
st.page_link('pages/P&E_Part_IV:_Energy_Creation,_Storage,_&_Transfer.py', label="Page 5: P&E 4 - Energy Creation, Storage & Transfer")
st.page_link('pages/P&E_Part_V:_Renewable_Energy.py', label="Page 6: P&E 5 - Renewable Energy")

st.header(' ',divider='grey')
st.title(':blue[Global Emissions by Decade from 1750-2020]')

st.write('This is a running system of maps including information on :blue[global emissions] using each decade from :blue[1750 to 2020] as marking points.')
st.write('The measurements for these maps are recorded in :blue[billions of tons of Carbon pollution], and for each respective map, the smallest circle represents :blue[0 billion tons] of pollution.')
st.write('It is important to note that the :blue[pollution] used for these maps consists solely of :blue[Carbon-Based pollution], some of which are the leading :blue[pollutants] that scientists know of today, emitting a staggering :blue[35 billion tons annually in CO2] alone.')

# Embedding video on pollution
if st.checkbox(':grey[One year of Carbon emissions.]'):
    st.video(data="https://youtu.be/7tTrGnoTqgo?si=VMI4MJEldyopqtrQ")
    st.write(":grey[Video from TIME on YouTube.]")

# Section for the year 1750
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1750')
if st.checkbox(':grey[Click to view map for 1750!]'):
    temp_data = pd.read_csv('data/emissions_1750.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[This map for global emissions from 1750 shows how little industrialization and large-scale production there was during this time, mony of the early maps in this segment will look similar as there was not much pollution being emitted when compared to the numbers of todays world.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[However, once you go through later maps, you will see this is most definitely not the case, and that the emitions that are being produced increase exponentially as the years go by.]')

# Section for the year 1760
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1760')
if st.checkbox(':grey[Click to view map for 1760!]'):
    temp_data = pd.read_csv('data/emissions_1760.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Being the fact that there are not as many countries from this time as there are today, along with the fact that this sort of data was much harder to collect back then, there are not many points of data to reference.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[Maps such as these truly help to visualize and understand the difference of the world today versus the world from centuries ago when technology was not nearly as prevalent as it is today.]')

# Section for the year 1770
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1770')
if st.checkbox(':grey[Click to view map for 1770!]'):
    temp_data = pd.read_csv('data/emissions_1770.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Still not much happening in terms of global pollution at this stage, especially when it is being compared to the global pollution that is output today.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[However, as we all know, one of the worlds leading pollution emitters, America, is going to be born this decade, so the map will become more exciting very soon.]')

# Section for the year 1780
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1780')
if st.checkbox(':grey[Click to view map for 1780!]'):
    temp_data = pd.read_csv('data/emissions_1780.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[As we can see, the process of reaching the amount of global emissions that we produce today drags on for a very long time, and then all of a sudden, they skyrocket.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[Now, showing all of these maps where there are seemingly zero emissions is not for no good reason, but it is really to show how little of time it took for us to pollute the entire world.]')

# Section for the year 1790
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1790')
if st.checkbox(':grey[Click to view map for 1790!]'):
    temp_data = pd.read_csv('data/emissions_1790.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Still looking the same as the previous maps, but little does the world know they are on the verge of an industrial revolution in just a few short decades, which will in turn launch the global emissions epidemic.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[The 1790 decade was a decade full of economic growth for the United States, with new bills being created that would accelerate the industrial growth of America.]')

# Section for the year 1800
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1800')
if st.checkbox(':grey[Click to view map for 1800!]'):
    temp_data = pd.read_csv('data/emissions_1800.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[We have finally reached a new century, and one that will bring widespread change and innovation across the entire world.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[To get an idea of the timeframe, this is the era that Napoleon embarked on his conquests. Which this may seem like a very long time ago, but in terms of the entire human existence, it was no less that a few hours ago.]')

# Section for the year 1810
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1810')
if st.checkbox(':grey[Click to view map for 1810!]'):
    temp_data = pd.read_csv('data/emissions_1810.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[More countries are just beginning to embark on their discoveries and integration of industrialization, and many of them will prove to be great contributors in the global emission epidemic.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[In this decade, the event that likely led to the the most pollution was the war of 1812. All wars are extremely polluting for the earth, not just from the emissions from the machines they use, but also all of the manmade objects and oils that are left behind on battlefields.]')

# Section for the year 1820
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1820')
if st.checkbox(':grey[Click to view map for 1820!]'):
    temp_data = pd.read_csv('src/data/emissions_1820.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[1820 is pretty much where it all changes, this is the decade where the industrial revolution really takes off, anf with that, America needed a faster way to travel around the country.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[With the boom of the industrial revolution came the implementation of thousands of miles of railroad tracks, and the coal-powered engines the trains were equipped with pumped out carbon pollution as fast as they burned the coal. However, this would only be the start of the industrial revolution, and all of the pollution that will come with it.]')

# Section for the year 1830
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1830')
if st.checkbox(':grey[Click to view map for 1830!]'):
    temp_data = pd.read_csv('data/emissions_1830.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[As you can see, there are many more red dots on this map than previous ones. This would likely be because many countries are beginning to industrialize, and therefore have a higher output of emissions that is now measureable.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[Machines became a big part of countries manufacturing processes, and in America the railroad system was growing at an exponential rate. This was also the era when the Opium Wars in Asia occurred, and we know that wars leave a lot of pollution behind.]')

# Section for the year 1840
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1840')
if st.checkbox(':grey[Click to view map for 1840!]'):
    temp_data = pd.read_csv('data/emissions_1840.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[There is not much of a difference in this map as compared to 1830, mostly because it is being compared to the emissions today, which make the emissions of this time seemingly 0. Yes, there is rapid advancement accross the world at this time, but the advancement is tremendously slow compared to the advancement of the late 20th to early 21st centuries.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[Rest assured, emissions are still rising at this point in time, and if we were only comparing maps from 1750-1850, this map would have a lot bigger of circumference to represent the rise in emissions. However it is all a matter of relativity, and the emissions relative to that time period really are not comparable at all unless you are using that time period to show the enormity of emissions today(almost like what this entire site is about).]')

# Section for the year 1850
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1850')
if st.checkbox(':grey[Click to view map for 1850!]'):
    temp_data = pd.read_csv('data/emissions_1850.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Still not much change with this map, but in this decade there is new technology on the rise, some of which has to do with emissions and pollution, such as the invention propylene.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[War was still polluting the world, as tensions in the Crimean war were rising, and the second Opium War was on the brink of commencement.]')

# Section for the year 1860
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1860')
if st.checkbox(':grey[Click to view map for 1860!]'):
    temp_data = pd.read_csv('data/emissions_1860.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[After the 1850 decade, emissions really began to skyrocket, and after this map we should begin to see larger and larger circles.l]')
    st.map(map_data, size='Emissions')
    st.write(':blue[There were still many global conflicts, but the Industrial Revolution was beginning to start its prime years, and the world would soon see change and technology that would never be reversed.]')

# Section for the year 1870
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1870')
if st.checkbox(':grey[Click to view map for 1870!]'):
    temp_data = pd.read_csv('data/emissions_1870.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[We are finally beginning to see our first spike in circle size, and as you can see that is located in the United Kingdom. Finally, a number big enough to compare to the monstrous emissions let out in the world today.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[We see the United Kingdom jump first, likely because of highly industrialized areas and cities full of industrial plants and factories, much like the area of Birmingham, England during this time period.]')

# Section for the year 1880
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1880')
if st.checkbox(':grey[Click to view map for 1880!]'):
    temp_data = pd.read_csv('data/emissions_1880.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[As the global population continued to rise, especially that in the United Kingdom, the demand for supplies would also rise.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[This causes the UK to continue rising in emissions due to the enormity of product that was coming out of the area, making early Englad one of the main contributors to early global emissiobs, but that would change relatively quickly.]')

# Section for the year 1890
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1890')
if st.checkbox(':grey[Click to view map for 1890!]'):
    temp_data = pd.read_csv('data/emissions_1890.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Just before the turn of the decade, one of the most influential decades in terms of where the world is headed towards in the coming decades.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[With the invention motion pictures, and even the first Olympic Games, show early signs of the fame-centric and money-driven lifestyles that we see today. The same money-driven lifestyles that create more wealth at the cost of the environment.]')

# Section for the year 1900
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1900')
if st.checkbox(':grey[Click to view map for 1900!]'):
    temp_data = pd.read_csv('data/emissions_1900.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[The 1900s. A seemingly new world in terms of technology, innovation, and potential that the world held. It was the beginning of a new era that would leave the old world unrecognizable.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[Pollution was really on the rise at this point, but the unfortunate reality is, there were not studies or scientists back then to tell the people that what they were doing was hurting the environment. Even at that point though, how many people in positions powerful enough to invoke proper change would have really listened?]')

# Section for the year 1910
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1910')
if st.checkbox(':grey[Click to view map for 1910!]'):
    temp_data = pd.read_csv('data/emissions_1910.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Global tensions have been nowhere near stable the last couple decades, and a long overdue World War I was underway. It was a new era of machines, and warfare was fought in a way never imagined before.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[With these new ways of warfare combined with the tensions that have been waiting to snap, an all-polluting, devastatingly deadly war occurred, leaving a massive scar on the world. However, this scar would be nothing compared to that of the bigger brother, World War II.]')

# Section for the year 1920
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1920')
if st.checkbox(':grey[Click to view map for 1920!]'):
    temp_data = pd.read_csv('data/emissions_1920.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Now that the first World War had ended, each major world power was now in a race with the other to innovate and industrialize as rapdily as possible.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[From here on out there is an exponential increase in global pollution overall, and with the aid of the highly economically-motivated world of the Roaring 20s, global pollutions would reach all-time highs.]')

# Section for the year 1930
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1930')
if st.checkbox(':grey[Click to view map for 1930!]'):
    temp_data = pd.read_csv('data/emissions_1930.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[As tensions had not gotten any better from the first World War, each country was still in a race to be number one, and with this, tensions and emissions had no choice but to continue being strained.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[After many series of invasions around the world, the globe would fall into its second World War at the end of the decade, paving way for pollution to take over the natural world.]')

# Section for the year 1940
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1940')
if st.checkbox(':grey[Click to view map for 1940!]'):
    temp_data = pd.read_csv('data/emissions_1940.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[The early 1940s saw some of the worst, most most unimaginable warfare possible, filled with record-breaking deaths and polluting every inch of the world. With war and tensions at the peak of what they have ever been in humanity, there was no time for any country to think about the impacts the billions of dollars in manufacturing that were spent would have on the environment.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[This was a decade that the world truly never was able to fully recover from, anything from oil spilled by the bombing of pearl harbor to warships in the middle of the ocean can be found, still releasing their effects on the surrounding environment.]')

# Section for the year 1950
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1950')
if st.checkbox(':grey[Click to view map for 1950!]'):
    temp_data = pd.read_csv('data/emissions_1950.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Just as the 1950s was about to begin, one of the longest wars in the history of the world would take place, and it would place the world in a standstill not only economically, but even with the every day lives of citizens.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[A war that would go on for decades was structured in the 1950s with mass production of nuclear weaponry, without any idea of when, or if, they would be used. This mass production of warheads is a major reason why global emissions rise greatly through these past two decades, and why they will continue to rise for decades to come.]')

# Section for the year 1960
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1960')
if st.checkbox(':grey[Click to view map for 1960!]'):
    temp_data = pd.read_csv('data/emissions_1960.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[The most noticeable difference in this map is the amount of polltuion that Russia is emitting for this year, which is no suprise with the Cold War having just begun.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[During this time period, two of the biggest world powers, Russia and the United States, were in an arms race against one another. The sheer amount of weaponry, vehicles, and nuclear warheads manufactured this time led to the great rise in emissions that we see during this time period.]')

# Section for the year 1970
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1970')
if st.checkbox(':grey[Click to view map for 1970!]'):
    temp_data = pd.read_csv('data/emissions_1970.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[With the Cold War at the height of its tensions and manufacturing, we see the biggest jump in pollution to date, so much that emissions have nearly doubled by this decade from the last.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[The United States and Russia have continued to research, develop, and manufacture nuclear warheads for the past two decades. New innovations and discoveries led to faster, cheaper manufacturing processes, accelerating the rise of global pollutions to a new rate.]')

# Section for the year 1980
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1980')
if st.checkbox(':grey[Click to view map for 1980!]'):
    temp_data = pd.read_csv('data/emissions_1980.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[As we reach closer to the modern world, we begin to see that more countries are begining to contribute overall to global pollution. In China, pollution is on the rise as the economy and industrialization of the country flourish.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[Overall, every world power is contributing significant pollution during this time. However, it seems as though no other country will reach the enormous numbers that the United States and Russia are able to put out...]')

# Section for the year 1990
st.header(' ',divider='grey')
st.header('Map of emissions in the year 1990')
if st.checkbox(':grey[Click to view map for 1990!]'):
    temp_data = pd.read_csv('data/emissions_1990.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[The Cold War has been at a seeming standstill for years, and it is on the brink of ending as the Soviet Union is beginning to fizzle out.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[Emissions overall have not changed much over the last decade, except for those of China which have doubled since the last decade. This is because the economy of China was beginning to boom at this time, and if they were going to continue as a major contributor to global trade, they would need to ramp up manufacturing.]')

# Section for the year 2000
st.header(' ',divider='grey')
st.header('Map of emissions in the year 2000')
if st.checkbox(':grey[Click to view map for 2000!]'):
    temp_data = pd.read_csv('data/emissions_2000.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[China is continuing to develop their economy, and manufacturing is at an all time high. At this point, China has replaced Russia as the second most world polluter, but that is by no coincidence.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[Since the fall of the Soviet Union in the early 90s, Russia saw a long period of economic decline, which is likely due to the extremely lessened amount of emissions that they have put out in the 2000s. With that, China was now able to enstate itself as one of the major powers of the world, and continues to be a leader in global trade.]')

# Section for the year 2010
st.header(' ',divider='grey')
st.header('Map of emissions in the year 2010')
if st.checkbox(':grey[Click to view map for 2010!]'):
    temp_data = pd.read_csv('data/emissions_2010.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[At this point, China has completely overtaken every world power in terms of pollution, reporting record numbers and even deaths due to respiratory illnesses among citizens. Although, worldwide, pollution is still getting worse every single year.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[However, in the Untied States, new movements for clean energy and the reduce of emissions and pollution overall will help reduce pollution in the future, but not by enough to make a major difference in the effects it has on the environment.]')

# Section for the year 2020
st.header(' ',divider='grey')
st.header('Map of emissions in the year 2020')
if st.checkbox(':grey[Click to view map for 2020!]'):
    temp_data = pd.read_csv('data/emissions_2020.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Current day; China continues to break records of pollution each year, so the efforts of policies from organizations such as the United Nations have little effect, and the reduced pollution by other countries have been replaced with even more pollution.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[It is a cycle that is never going to end until everyone works together and recognizes the real problems in this situation. Websites such as these will continue to help educate those on the effects of pollution, and ultimately climate change, until the time comes where real change can come into effect.]')

st.subheader(' ',divider='grey')
if st.checkbox(":grey[Click to view informational videos on global emissions and warming.]"):
    st.video(data='https://youtu.be/LxgMdjyw8uw?si=k80g90_j-mt8QPow')
    st.write(':grey[Video from Kurzgesagt on YouTube.]')
    st.video(data='https://youtu.be/7tTrGnoTqgo?si=VMI4MJEldyopqtrQ')
    st.write(':grey[Video from TIME on YouTube.]')
    st.subheader(' ',divider='grey')
    st.video(data='https://youtu.be/yhlg9txl7yM?si=1_MBa9roBaTFrmG8')
    st.write(':grey[Video from The Economist on YouTube.]')
    st.subheader(' ',divider='grey')
    st.video(data='https://youtu.be/n7onPTCZ1Ws?si=AtKANh93v_faf3ox')
    st.write(':grey[Video from Cambridge University on YouTube.]')
st.subheader(' ',divider='grey')