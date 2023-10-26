import folium
import os, base64, random
from config import Config
from statistics import mean
from geopy.geocoders import Nominatim

# Create a map
def get_map(ufarms, query):
    m = folium.Map(tiles='stamenwatercolor', location=[0, 0], zoom_start=2)

    # Create a geocoder instance (Nominatim in this example)
    geolocator = Nominatim(user_agent="myGeocoder")

    try:
        # Perform geocoding -- replace string with search bar text
        location = geolocator.geocode(query)
        
        if location:
            # Add a marker to the map using the geocoded coordinates
            folium.Marker([location.latitude, location.longitude], popup="Google HQ").add_to(m)
        else:
            print("Location not found")

    except Exception as e:
        print("An error occurred:", str(e))

    # Save or display the map
    m.save(os.path.join(Config.TEMPLATE_PATH, "testmap.html"))
