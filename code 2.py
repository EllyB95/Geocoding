# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 01:34:46 2024

@author: harpr

https://www.datacamp.com/tutorial/geocoding-for-data-scientists
"""
#%%
import pandas as pd
import geopy
#%%
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="bainselly95@gmail.com")
Address_table=pd.DataFrame()
Street = input("Enter the Street Address")
City = input("Enter the City Name")
State = input("Enter the State name")
Country = input("Country name")
address1_osm= (str(Street)+" "+str(City)+" "+str(State)+" "+str(Country))
print(address1_osm)
location = geolocator.geocode(address1_osm)
print(location)
print('Latitude: '+str(location.latitude)+', Longitude: '+str(location.longitude))
#%%
Address = pd.DataFrame({'Street':[Street],'City':[City],'State':[State],'Country':[Country]})
DF=pd.concat([Address_table,Address])
#%%