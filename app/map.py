import folium
import os, base64, random
from config import Config
from statistics import mean

def get_map(ufarms, coordinates=None, address=None):
    print("Map")
    lats = []
    lons = []

    for farm in ufarms:
        lats.append(farm.Privacy_lat)
        lons.append(farm.Privacy_lon)

    if coordinates:
        # Add a marker to the map at the provided coordinates
        # tiles='stamenwatercolor' currently not working from the provider
        m = folium.Map(width=750,height=1000, location=coordinates, zoom_start=13)
    else:
        print("Coordinates not provided.")
        m = folium.Map(width=750,height=1000, location=[mean(lats), mean(lons)], zoom_start=13)

    # Global tooltip
    # tooltip = 'Click For More Info'

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
    #    create marker elements
    for farm in ufarms:
        if farm.IsActive == 1: 
            icon_color = 'green'
        else: 
            icon_color = 'orange'
        icon=folium.Icon(color=icon_color, icon='leaf', prefix='fa')
        encoded = base64.b64encode(open(Config.STATIC_PATH + f'plot{random.randint(1, 4)}.png', 'rb').read())

        html = """
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=yes">
                    <!-- Jquery -->
                    <script src="https://code.jquery.com/jquery-3.7.0.min.js" integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g=" crossorigin="anonymous"></script>
                    <!-- Font Awesome -->
                    <script src="https://kit.fontawesome.com/64910da04b.js" crossorigin="anonymous"></script>
                    <!-- Bootstrap CSS -->
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                    <title>IFrame</title>
                </head>
                """
        img = '<img src="data:image/png;base64,{}" width="180" height="110">'.format
        ## findme # copy email on click button request todo
        # profile_url = 'https://example.com/profile' todo

        if farm.Contact == "m.ehler@comcast.net":
            # iframe_content = open(Config.TEMPLATE_PATH + 'iframe_content.html', 'r').read()  Attepmted to build from existing template
            js_code = """
                    <script>
                        function redirectParentPage() {
                            parent.location.href = "/profile";
                        }
                    </script>
                    """
            # thumbnail_body = f"""
            #     <!DOCTYPE html>
            #     <html>
            #     <head>
            #         <title>IFrame</title>
            #     </head>
            #     <body>
            #         {iframe_content}
            #         <!-- Rest of your HTML content -->
            #     </body>
            #     </html>
            #     """
            thumbnail_body = f"""
                <!DOCTYPE html>
                <html>
                {html}
                <body>
                    <div>
                        <h3><a data-auto-recognition="true" href="http://127.0.0.1:5000/profile"></i><span id='HostName'> {farm.Name} </span></a><h5>
                        <b>Contact: <a data-auto-recognition="true" href="mailto:m.ehler@comcast.net" class="wixui-rich-text__text"><span id='Contact'> {farm.Contact} </span></a>
                        <br>Work Request: {farm.Request} </b></h5>
                    </div>
                </body>
                {img(encoded.decode('UTF-8'))}
                {js_code}
                </html>
                """
        else:
            thumbnail_body = f"""
                            <!DOCTYPE html>
                            <html>
                            {html}
                            <h3>{farm.Name}</h3><h5><b>Contact: {farm.Contact} <br>Work Request: {farm.Request}</b></h5> {img(encoded.decode('UTF-8'))}
                            """
        resolution, width, height = 20, 12, 7
        iframe = folium.IFrame(thumbnail_body, width=(width*resolution)+20, height=(height*resolution)+100)
        popup = folium.Popup(iframe, max_width=860, max_height=640 )
        marker = folium.Marker(location=[farm.Privacy_lat, farm.Privacy_lon], popup=popup, icon=icon)
        marker.add_to(m)

        folium.Circle(location= [farm.Privacy_lat, farm.Privacy_lon],
                    radius=300,
                    weigth=1,
                    color=icon_color,
                    fill=True).add_to(m)
        # Add the legend to the map
        m.get_root().html.add_child(folium.Element(legend_html))
        #Save Map HTML to template
        m.save(os.path.join(Config.TEMPLATE_PATH, 'map.html'))   
    # END