import requests
from config import Config

# Function to geocode an address using Mapbox
def geocode_address(partial_address):
    base_url = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    params = {
        "access_token": Config.MAPBOX_TOKEN,
        "autocomplete": True,  # Enable autocomplete to handle incomplete addresses
        "limit": 1,  # Limit the results to the first match
        "types": "address",  # Filter results to only addresses
        "language": "en",  # Set the language for the response
        "text": partial_address,  # The partial address to search for
    }

    response = requests.get(f"{base_url}/{partial_address}.json", params=params)

    if response.status_code == 200:
        data = response.json()
        if data["features"]:
            result = data["features"][0]
            place_name = result["place_name"]
            coordinates = result["center"]

            print(f"Place Name: {place_name}")
            print(f"Coordinates: {coordinates}")
        else:
            print("No results found.")
    else:
        print("Failed to retrieve data from the Mapbox Geocoding API.")

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
