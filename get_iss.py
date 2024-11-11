import urllib.request
import json


def iss_loc():
    url='http://api.open-notify.org/iss-now.json'
    
    request = urllib.request.urlopen(url)
    result=json.loads(request.read())

    #print(result)

    # Pass the latitude and longitude of this endpoint to google maps

    lat = result['iss_position']['latitude']
    lon = result['iss_position']['longitude']


    print("Google Map: ","https://www.google.com/maps/place/"+lat +"+"+lon )
    return lat,lon
