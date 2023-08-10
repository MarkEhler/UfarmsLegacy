import folium
import os, csv, base64, random
from config import Config
from statistics import mean
import pandas as pd
from azure.storage.blob import BlobServiceClient

# make into class todo
def get_map():
    # Connect to your Azure Blob Storage
# Connect to your Azure Blob Storage
    connection_string = "DefaultEndpointsProtocol=https;AccountName=ufarmsblob;AccountKey=z96iS7OjIMrYWh0xGTrL9diKawtvA6SevWEFX038BXhhbVyzxfrGjYmWijwtFHwJ1bZTHeGDKcgz+AStgo/8ew==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(BLOB_CNX_STRING)

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
            <p style="color: orange;"><span style="color: #87CEEB;"></span> No Openings</p>
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

            fname = "map.py"
            dn = os.path.abspath(fname)
            print(os.path.dirname(dn), end="\n:)\n")
            print(Config.STATIC_PATH)
            print(Config.STATIC_PATH + f'plot{random.randint(1, 4)}.png')
            try:
                encoded = base64.b64encode(open(Config.STATIC_PATH + f'plot{random.randint(1, 4)}.png', 'rb').read())
            except:
                encoded = base64.b64encode(open(f'/app/app/static/plot{random.randint(1, 4)}.png', 'rb').read())
            
                #'/Ufarms/app/static/plot2.png'
            #'/home/markee/ufarms/Ufarms/app/static/plot4.png'
            #'os.path.join(Config.STATIC_PATH,f'plot{random.randint(1, 4)}.png')'
            html = '<img src="data:image/png;base64,{}" width="180" height="110">'.format
            #copy email on click button request todo
            if row.loc['contact'] == "m.ehler@comcast.net":
                # todo url_for() not defined                                                                
                thumbnail_body = """
                <!DOCTYPE html>
                <head>

                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=yes">
                <style> img { max-width: 100%; } </style>
                <!-- Jquery -->
                <script src="https://code.jquery.com/jquery-3.7.0.min.js" integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g=" crossorigin="anonymous"></script>
                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                
                    <title>IFrame</title>
                <script>
                function redirectTo(url) {
                    window.location.href = url;
                }
                </script>
                </head>
                <body>
                    <div>
                        <h3><a class="btn btn-default" onclick="redirectTo(profile)">""" + f"""</i><span id='HostName'> {row['name']} </span></a></h3>
                        <b>Contact: <a data-auto-recognition="true" href="mailto:m.ehler@comcast.net" class="wixui-rich-text__text"><span id='textToCopy'> {row.loc['contact']} </span></a>
                        <br>Work Request: {row['request']} </b>

                    </div>
                </body>
                </html>{html(encoded.decode('UTF-8'))}"""
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
    m.save(Config.TEMPLATE_PATH + f'map.html')
    # Create custom marker icon
    #logoIcon = folium.features.CustomIcon('{Config.STATIC_PATH}', icon_size=(50, 50))

    # Vega data
    #vis = os.path.join('data', 'vis.json')

    # Geojson Data
    #overlay = os.path.join('data', 'overlay.json')