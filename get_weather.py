import urllib.request
import json



def get_weather(lat,lon):
    key='d013bec7a46610781904838bced9f57a'
    url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'

    request = urllib.request.urlopen(url)
    result=json.loads(request.read())

    return result

