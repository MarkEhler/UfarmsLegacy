from geopy.geocoders import Nominatim
import csv #( findme later connect to db)
import pandas as pd

#make into class todo
debug = False # replace with env variable
df = pd.read_csv(f'data/test_hosts.csv')
df['zipcode'] = df['zipcode'].apply(str)
address_strs = []
privacy_lats = []
privacy_lons = []
for (index, row) in df.iterrows():
    # must add row back to df?
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(f"{row.loc['address1']} {row.loc['city']} {row.loc['state']}, {str(row.loc['zipcode'])}")
    row.loc['address_str'] = getLoc.address.split(",")
    address_strs.append(getLoc.address.split(","))
    #get general location for privacy
    loc = Nominatim(user_agent="GetLoc")
    neighborhood = row.loc['address_str'][-6:]
    getLoc = loc.geocode(f"{neighborhood}")
    privacy_lats.append(float(getLoc.latitude))
    privacy_lons.append(float(getLoc.longitude))
    #todo add logic for handling locations that are created on top of other locations so that they show on the map
df['address_str'] = address_strs
df['privacy_lat'] = privacy_lats
df['privacy_lon'] = privacy_lons

print(df.columns)
df.to_csv('data/hosts_w_locations.csv')
