import folium
import os, csv, base64
from statistics import mean, pstdev
import pandas as pd


df = pd.read_csv('data/hosts_w_locations.csv')
locations = []
lats = []
lons = []

for (index, row) in df.iterrows():
    locations.append(row)
    lat = float(row.loc['privacy_lat'])
    lon = float(row.loc['privacy_lon'])
    lats.append(lat)
    lons.append(lon)

    std_lat = pstdev(lats)
    std_lon = pstdev(lons)
    # Create map object findme location is the mean of all lat, lons, zoom start is the std but inverse of 12 max
m = folium.Map(tiles='stamenwatercolor', width=750,height=1000, location=[mean(lats), mean(lons)], zoom_start=14)


# Global tooltip
tooltip = 'Click For More Info'


#for (i, col) in enumerate(df):
#    print(df[col], 'just col', '\n')

for (i, row) in df.iterrows():
    if row['host'] == 1:
        if row['isactive'] == True: 
            icon_color = 'green'
        else: 
            icon_color = 'orange' 
        iframe = folium.IFrame(str(row.loc['name']) + '<br>' + 'Contact: ' + row.loc['contact'] + '<br>')
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(location=[row.loc['privacy_lat'], row.loc['privacy_lon']], icon=folium.Icon(color=icon_color, icon='leaf', prefix='fa'), popup=popup).add_to(m)

   