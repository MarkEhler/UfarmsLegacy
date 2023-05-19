import folium
import os, csv, base64, random, settings
from statistics import mean, pstdev
import pandas as pd
import branca

# make into class todo
def get_map():
# get cached host nodes
# \\wsl.localhost\Ubuntu\home\markee\ufarms\Ufarms\app\data\hosts_w_locations.csv
    df = pd.read_csv("app\data\hosts_w_locations.csv")
    print(df)
    locations = []
    lats = []
    lons = []

    for (index, row) in df.iterrows():
        locations.append(row)
        lat = float(row.loc['privacy_lat'])
        lon = float(row.loc['privacy_lon'])
        lats.append(lat)
        lons.append(lon)
    
    print(lats, lons)
    # Create map object findme location is the mean of all lat, lons, zoom start is the std but inverse of 12 max
    m = folium.Map(tiles='stamenwatercolor', width=750,height=1000, location=[mean(lats), mean(lons)], zoom_start=13)


    # Global tooltip
    tooltip = 'Click For More Info'
    # Define the legend HTML
    legend_html = '''
        <div style="position: fixed;
                    bottom: 50px; left: 50px; width: 120px; height: 90px;
                    border:2px solid grey; z-index:9999; font-size:14px;
                    background-color:white; opacity:0.8">
            <p><strong>Legend</strong></p>
            <p style="color: green;"><span style="color: green;"></span> Openings</p>
            <p style="color: orange;"><span style="color: #87CEEB;"></span> Check Back Soon</p>
        </div>
    '''

    # Add the legend to the map
    m.get_root().html.add_child(folium.Element(legend_html))

    for (i, row) in df.iterrows():
        if row['host'] == 1:
            if row['isactive'] == True: 
                icon_color = 'green'
            else: 
                icon_color = 'orange'
            icon=folium.Icon(color=icon_color, icon='leaf', prefix='fa')
            resolution, width, height = 20, 12, 7
            encoded = base64.b64encode(open(os.path.join(settings.STATIC_PATH,f'plot{random.randint(1, 4)}.png'), 'rb').read())
            html = '<img src="data:image/png;base64,{}" width="180" height="110">'.format
            iframe = folium.IFrame(f"<h3>{row['name']}</h3><h4>Contact: {row.loc['contact']} <br>Work Request: {row['request']} </h4> {html(encoded.decode('UTF-8'))}", width=(width*resolution)+20, height=(height*resolution)+100)
            popup = folium.Popup(iframe, max_width=640, max_height=360 )
            marker = folium.Marker(location=[row.loc['privacy_lat'], row.loc['privacy_lon']], popup=popup, icon=icon)
            print(marker)
            marker.add_to(m)

            folium.Circle(location= [row.loc['privacy_lat'], row.loc['privacy_lon']],
                        radius=300,
                        weigth=1,
                        color=icon_color,
                        fill=True).add_to(m)
        
    m.save(f'{settings.TEMPLATE_PATH}/map.html')
    # Create custom marker icon
    #logoIcon = folium.features.CustomIcon('{STATIC_PATH}', icon_size=(50, 50))

    # Vega data
    #vis = os.path.join('data', 'vis.json')

    # Geojson Data
    #overlay = os.path.join('data', 'overlay.json')
#todo set tooltip box size

#todo add photos of locations
#todo add contact links to test_hosts.csv
#todo links to dynamic profile page
#columns=['ID', 'name', 'address1', 'address2', 'city', 'state', 'zip', 'request', 'string address' 'lat', 'lon', 'work reuest status', 'photo_key']
'''
    resolution, width, height = 75, 7, 3
    encoded = base64.b64encode(open(os.path.join(settings.STATIC_PATH,'mark_pic.jpg'), 'rb').read())
    # geolocation from the generated lat, lon
    for i in locations:
        if i[8] == 'TRUE': 
            icon_color = 'green'
        else: 
            icon_color = 'orange' 
        
        folium.Marker([float(i[-2].strip('"')), float(i[-1].strip('"'))],
            popup=folium.Popup(f"<strong>{i[1]}<br><br>Contact: {i[9]}</strong>", width=500, height=250),
            tooltip=tooltip,
            icon=folium.Icon(color=icon_color, icon='leaf', prefix='fa')).add_to(m),
    


    html = '<img src="data:image/jpg;base64,{}">'.format
    iframe = folium.IFrame(html(encoded.decode('UTF-8')), width=(width*resolution)+20, height=(height*resolution)+20)
    popup = folium.Popup(iframe, max_width=2650)
    marker = folium.Marker(location=[float(i[-2].strip('"')), float(i[-1].strip('"'))], popup=popup, icon=icon)
    marker.add_to(m)

       
    '''
'''
    folium.Marker([42.375140, -71.032450],
                popup='<strong>Location Five</strong>',
                tooltip=tooltip,
                icon=logoIcon).add_to(m),
                
                Use the following to add thumbnails
    '''

