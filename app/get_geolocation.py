from geopy.geocoders import Nominatim
import csv #( findme later connect to db)

#make into class todo
debug = False # replace with env variable
with open('data/test_hosts.csv', newline='') as csvfile:
    read_in = csv.reader(csvfile, delimiter=',', quotechar='|')
    locations = []
    for row in read_in:
        locations.append(row)

# calling the Nominatim tool
# entering the location name
for i in locations:
    loc = Nominatim(user_agent="GetLoc")
    name=i[0]
    address1=i[2]
    #address2=i[3]
    city=i[4]
    state=i[5]
    zipcode=i[6]
    if debug == True:
        print(f"{address1} {city} {state} {zipcode}", "\n")
    getLoc = loc.geocode(f"{address1} {city} {state}, {zipcode}")
    i.append(getLoc.address)
    i.append(float(getLoc.latitude))
    i.append(float(getLoc.longitude))

    
#columns=['name', 'host', 'address1', 'address2', 'city', 'state', 'zip', 'request', 'lat', 'lon']
'''
[["Shelbourn Farmer's Market", '2', 'Church St', '', 'Shelburne', 'VT', '05482', 'vendor', 44.3780193, -73.2275125], 
["Burlington Farmer's Market", '1', '345 Pine St Burlington', '', 'Burlington', 'VT', '05401', 'vendor', 44.4693561, -73.2161314], 
['City Market / Onion River Co-op', '1', '82 S Winooski Ave', '', 'Burlington', 'VT', '05401', 'watering', 44.47803611764706, -73.21097505882354], 
['Intervale Community Farm', '1', '232 Intervale Road', '', 'Burlington ', 'VT', '05401', 'planting', 44.499452166964346, -73.20794710638079], 
['Vermont Community Garden Network', '1', '1 Mill St', '#200', 'Burlington', 'VT', '05401', 'building beds', 44.48835, -73.186553]]
'''
with open('data/hosts_w_locations.csv', 'w') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    #wr.writerow(columns)
    wr.writerows(locations)