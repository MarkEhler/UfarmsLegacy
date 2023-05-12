import folium
import os, csv, settings
from statistics import mean
# make into class todo
def get_map(DATA_PATH):
# get cached host nodes "\\wsl.localhost\Ubuntu\home\markee\ufarms\Ufarms\app\data\hosts_w_locations.csv"
    with open(f'{DATA_PATH}hosts_w_locations.csv', newline='') as csvfile:
        read_in = csv.reader(csvfile, delimiter=',', quotechar='|')
        locations = []
        lats = []
        lons = []
        for row in read_in:
            locations.append(row)
            lat = float(row[-2].strip('"'))
            lon = float(row[-1].strip('"'))
            lats.append(lat)
            lons.append(lon)
    # Create map object findme location is the mean of all lat, lons, zoom start is the std but inverse of 12 max
    m = folium.Map(location=[mean(lats), mean(lons)], zoom_start=12)


    # Global tooltip
    tooltip = 'Click For More Info'

    # Create custom marker icon
    #logoIcon = folium.features.CustomIcon('{STATIC_PATH}', icon_size=(50, 50))

    # Vega data
    #vis = os.path.join('data', 'vis.json')

    # Geojson Data
    #overlay = os.path.join('data', 'overlay.json')
#todo set tooltip box size
#todo add photos of locations
#todo add contact links to test_hosts.csv
#todo add joined address to w_locations.csv
    for i in locations:
        # geolocation from the generated lat, lon
        folium.Marker([float(i[-2].strip('"')), float(i[-1].strip('"'))],
            popup=f'<strong>{str(i[0])}<br>{i[2]}</strong>',
            tooltip=tooltip,
            icon=folium.Icon(color='green', icon='leaf', prefix='fa')).add_to(m),


    '''
    folium.Marker([42.375140, -71.032450],
                popup='<strong>Location Five</strong>',
                tooltip=tooltip,
                icon=logoIcon).add_to(m),
                
                Use the following to add thumbnails
    folium.Marker([42.315140, -71.072450],
                popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m)
    '''
    # Generate map
    m.save(f'{settings.TEMPLATE_PATH}/map.html')
