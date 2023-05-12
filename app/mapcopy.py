import folium
import os, csv

with open(f'data/hosts_w_locations.csv', newline='') as csvfile:
    read_in = csv.reader(csvfile, delimiter=',', quotechar='|')
    locations = []
    for row in read_in:
        locations.append(row)


# Create map object findme location is the mean of all lat, lons, zoom start is the std but inverse of 12 max
m = folium.Map(location=[44, -73], zoom_start=10)

# Global tooltip
tooltip = 'Click For More Info'

# Create custom marker icon
#logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50, 50))

# Vega data
#vis = os.path.join('data', 'vis.json')

# Geojson Data
#overlay = os.path.join('data', 'overlay.json')

# Create markers
for i in locations:
    # geolocation from the generated lat, lon

    folium.Marker([float(i[-2].strip('"')), float(i[-1].strip('"'))],
        popup=f'<strong>{i[0]}</strong>',
        tooltip=tooltip,
        icon=folium.Icon(color='green', icon='<i class="fa fa-leaf" aria-hidden="true"></i>')).add_to(m),
'''
folium.Marker([42.375140, -71.032450],
            popup='<strong>Location Five</strong>',
            tooltip=tooltip,
            icon=logoIcon).add_to(m),
folium.Marker([42.315140, -71.072450],
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m)
'''
# Generate map
m.save('templates/map.html')