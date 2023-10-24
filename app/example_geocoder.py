import folium
from geopy.geocoders import Nominatim

# Create a map
m = folium.Map(location=[0, 0], zoom_start=2)

# Create a geocoder instance (Nominatim in this example)
geolocator = Nominatim(user_agent="myGeocoder")

# Perform geocoding -- replace string with search bar text -- in case of incomplete or mistyped address format string into useable address
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")

# Add a marker to the map using the geocoded coordinates
folium.Marker([location.latitude, location.longitude], popup="Google HQ").add_to(m)

# Save or display the map
m.save("map.html")