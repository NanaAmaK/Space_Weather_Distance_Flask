from flask import Flask, render_template
from get_iss import iss_loc
from get_weather import get_weather
from get_distance import dist
from get_reverse_geo import address
from get_country import country

app = Flask(__name__)

@app.route('/')
def home():
    # Get ISS data
    data = iss_loc()
    lat, lon = data[0], data[1]

    # Get weather data
    weather = get_weather(lat, lon)
    temp_c = round(weather["main"]["temp"] - 284.2, 2)
    description = weather["weather"][0]["description"]

    # Get country and flag
    add = address(lat, lon)
    country_code = add["countryCode"]
    if country_code:
        flag = country(country_code)[0]["flags"]["png"]
    else:
        country_code = "Over Water"
        flag = None

    # Calculating distance between my location and the ISS
    distance = dist(lat, lon, 46.5311503, -80.9497801)

    # Passing data to template
    return render_template('index.html', lat=lat, lon=lon, temp_c=temp_c, description=description, country_code=country_code, flag=flag, distance=distance)

if __name__ == "__main__":
    app.run(debug=True, port=5001)