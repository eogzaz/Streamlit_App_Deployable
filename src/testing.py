import streamlit as st
import pandas as pd
import numpy as np
import os
from collections import defaultdict

yes = 'data/real_data.csv'
new_data = []

def clean_data():
    with open(yes, 'r') as ems:
        for line in ems:
            items = line.split(',')
            n = items[2]
            if int(n) % 10 == 0:
                file = open('data/country_by_decade_emissions_real.txt', 'a')
                file.write(line)
                file.close()
                #new_data.append(line)


clean_data()
print(new_data)

no = 'data/total_emissions_global_2019.csv'

def coords():
    with open(no, 'r') as coords:
        for line in coords:
            dat = ''
            items = line.split(',')
            nation = items[0]
            lat = items[3]
            lon = items[4]
            dat = nation + ',' + lat + ',' + lon
            file = open('data/nations_coords.txt', 'a')
            file.write(dat)
            file.close()

#coords()

thing1 = 'data/country_by_decade_emissions.csv'
thing2 = 'data/nations_coords.csv'

def real_data():
    with open(thing1, 'r') as file1:
        for line in file1:
            item = line.split(',')
            with open(thing2, 'r') as file2:
                for lines in file2:
                    items = lines.split(',')
                    if item[0].lower() == items[0].lower():
                        file3 = open('data/come_on.txt', 'a')
                        new_list = ''
                        new_list = item[0] + ',' + item[2] + ',' + item[3] + ',' + items[1] + ',' + items[2]
                        file3.write(new_list)
                        file3.close()
real_data()

file1 = open('data/come_on.csv', 'r')

def cleaner():
    count = 0
    data = ''
    for thing in file1:
        if count % 2 == 0:
            count += 1
            with open('data/last_data.txt', 'a') as yup:
                yup.write(data)
                yup.close()
            data = ''
        else:
            count += 1
            data = data + thing

#cleaner()

#file1 = open('data/country_by_decade_emissions.txt', 'r')
#thing1 = file1.split('/n')
#file2 = open('data/last_data.txt', 'r')
#thing2 = file2.split('/n')

"""
if st.checkbox('Show map of Country Emissions by Decade(Million tons of C)'):
    check = slider
    df = pd.read_csv('data/country_by_decade_emissions.csv', dtype={"Year": str})
    map_data = pd.DataFrame(df, columns=['Emissions', 'Year', 'LAT', 'LON'])
    for items in df:
        item = items.split(',')
        if item[2] == slider:
            map_data = items
    if check == slider:
        st.map(map_data)
    else:
        map_data = pd.DataFrame(df, columns=['Emissions', 'Year', 'LAT', 'LON'])
"""
df = pd.read_csv('data/country_by_decade_emissions.csv', dtype={"Year": str})
dict1 = {"Emissions", "LAT", "LON"}
"""
file1 = open('data/country_by_decade_emissions.csv', 'r')
for years in slider_options:
    for my_data in file1:
        items = my_data.split(',')
        data_list = []
        if years == slider:
            data_list.append(items[3])
            data_list.append(items[4])
            data_list.append(items[5])
            #st.write(data_list)
            dict1["Emissions", "LAT", "LON"] = data_list
        else:
            dict1 = {"Emissions", "LAT", "LON"}
st.write(dict1)
"""


file1 = open('data/country_by_decade_emissions.csv', 'r')
file2 = open("data/temp_file.txt", "w")

new_data = '2000'
slider = '2000'
for my_data in file1:
    loop = ''
    items = my_data.split(',')
    if items[2] == slider:
        loop = f'{items[3]},{items[4]},{items[5]}'
        print(loop)
        file2.write(loop)
    loop = ''
file2.close()

checker = '1700'
slider = '1750'
slider_options = [1750,1760,1770,1780,1790,1800,1810,1820,1830,1840,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020]
file1 = open('data/country_by_decade_emissions.csv', 'r')
file2 = open("data/temp_file.csv", 'a')

new_data = ''
for number in slider_options:
    if checker != slider:
        os.remove('data/temp_file.csv')
        file2 = open("data/temp_file.csv", 'a')
        check = 0
        for my_data in file1:
            loop = ''
            items = my_data.split(',')
            if check == 0:
                headers = f'{items[3]},{items[4]},{items[5]}'
                file2.write(headers)
            check += 1
            if items[2] == slider:
                ems = int(items[3]) / 1000
                ems = round(ems)
                loop = f'{ems},{items[4]},{items[5]}'
                print(loop)
                file2.write(loop)
            loop = ''
            checker = slider
file2.close()
