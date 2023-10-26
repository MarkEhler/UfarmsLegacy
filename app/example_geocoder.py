import requests
from config import Config

# Function to geocode an address using Mapbox
def geocode_address(address):

    base_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json'
    params = {
        'access_token': Config.MAPBOX_TOKEN,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'features' in data and data['features']:
        # Extract coordinates from the first result
        coordinates = data['features'][0]['center'][::-1]
        return coordinates
    else:
        return None

#  next step extract the map generation for use with the address created
# Create a Folium map
# m = folium.Map(location=[0, 0], zoom_start=10)
# # Geocode the address
# coordinates = geocode_address(address)
# if coordinates:
#     # Add a marker to the map at the geocoded coordinates
#     folium.Marker(location=coordinates, popup=address).add_to(m)
# else:
#     print(f"Geocoding failed for address: {address}")

# # Save or display the map
# m.save('map.html')
