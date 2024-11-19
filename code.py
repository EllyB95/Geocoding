# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 01:34:46 2024

@author: harpr

https://www.datacamp.com/tutorial/geocoding-for-data-scientists
"""
#%%
import pandas as pd
import geopy

l_cols= ['Name','Street Address','City','State','Zipcode']
df = pd.read_csv('D:/geocoding/museums list CAN.csv', encoding = "ISO-8859-1",usecols=l_cols)
#%%
df['Country'] = 'Canada'
l_cols_concat = ['Street Address','City','State','Zipcode','Country']
df['unique_address'] = df['Name'].str.cat(others=df[l_cols_concat], sep=',',na_rep='')
df.head()
#%%
address1 = df['unique_address'].iloc[0]
#%%
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="bainselly95@gmail.com")
location = geolocator.geocode(address1)
print(location)
#%%
l_cols_concat = ['City','State','Country']
df['unique_address_osm'] = df['Street Address'].str.cat(others=df[l_cols_concat], sep=',',na_rep='')
address1_osm = df['unique_address_osm'].iloc[0]
#%%
address1_osm = df['unique_address_osm'].iloc[0]
#%%
location = geolocator.geocode(address1_osm)
print('Latitude: '+str(location.latitude)+', Longitude: '+str(location.longitude))
#%%