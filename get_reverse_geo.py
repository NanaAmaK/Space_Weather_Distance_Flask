import urllib.request
import json



def address(lat,lon):
    key='bdc_630a22908f8d4d71a7d2990962380ee4'
    url=f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={key}'
    request = urllib.request.urlopen(url)
    result=json.loads(request.read())
    return result