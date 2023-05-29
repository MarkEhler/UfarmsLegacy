import folium
import os, csv, base64, random, settings
from statistics import mean, pstdev
import pandas as pd
#import branca
from azure.storage.blob import BlobServiceClient

# make into class todo
def get_map():
    # Connect to your Azure Blob Storage
# Connect to your Azure Blob Storage
    connection_string = "DefaultEndpointsProtocol=https;AccountName=ufarmsblob;AccountKey=z96iS7OjIMrYWh0xGTrL9diKawtvA6SevWEFX038BXhhbVyzxfrGjYmWijwtFHwJ1bZTHeGDKcgz+AStgo/8ew==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    try:
        # Specify the container name and blob name of your CSV file in Azure Blob Storage
        container_name = 'mnt'
        blob_name = 'hosts_w_locations.csv'
        # Download the CSV file to a local temporary file
        local_file = '/tmp/hosts_w_locations.csv'
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        with open(local_file, "wb") as file:
            file.write(blob_client.download_blob().readall())

        # Read the CSV file
        df = pd.read_csv(local_file)
    except:
        print('error: ')
    
    locations = []
    lats = []
    lons = []

    for (index, row) in df.iterrows():
        locations.append(row)
        lat = float(row.loc['privacy_lat'])
        lon = float(row.loc['privacy_lon'])
        lats.append(lat)
        lons.append(lon)

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

            #print log for debug
            print(os.path.join(settings.STATIC_PATH,f'plot{random.randint(1, 4)}.png'))
            print(settings.APP_PATH)
            fname = "plot1.png"
            dn = os.path.abspath(fname)
            print(dn)
            print(os.path.dirname(dn), end="\n:)\n")
            try:
                encoded = base64.b64encode(open(os.path.join(settings.STATIC_PATH,f'plot{random.randint(1, 4)}.png'), 'rb').read())
            except:
                encoded = base64.b64encode(open(f'/app/app/static/plot{random.randint(1, 4)}.png', 'rb').read())
            
                #'/Ufarms/app/static/plot2.png'
            #'/home/markee/ufarms/Ufarms/app/static/plot4.png'
            #'os.path.join(settings.STATIC_PATH,f'plot{random.randint(1, 4)}.png')'
            html = '<img src="data:image/png;base64,{}" width="180" height="110">'.format
            #copy email on click button request todo
            if row.loc['contact'] == "m.ehler@comcast.net":
                thumbnail_body = f"<h3>{row['name']}</h3><h4>Contact: <a class='btn btn-default' onclick='redirectToURL()'><span> {row.loc['contact']} </span> <br>Work Request: {row['request']} </h4> {html(encoded.decode('UTF-8'))}"

            else:
                thumbnail_body = f"<h3>{row['name']}</h3><h4>Contact: {row.loc['contact']} <br>Work Request: {row['request']} </h4> {html(encoded.decode('UTF-8'))}"
           
            resolution, width, height = 20, 12, 7
            iframe = folium.IFrame(thumbnail_body, width=(width*resolution)+20, height=(height*resolution)+100)
            popup = folium.Popup(iframe, max_width=640, max_height=360 )
            marker = folium.Marker(location=[row.loc['privacy_lat'], row.loc['privacy_lon']], popup=popup, icon=icon)
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