
# Import Required Libraries
from datetime import datetime
import requests

# Define constants
api_key = "b556f5cfd4f374584d2888de30f3a41b"
geolocation_api_endpoint = "https://api.openweathermap.org/geo/1.0/direct"
weather_api_endpoint = "https://api.openweathermap.org/data/2.5/weather"

# Get location from user
location = input("Enter a location: ")

# Get latitude and longitude from geolocation API
geolocation_params = {"q": location, "appid": api_key}
try:
    response = requests.get(geolocation_api_endpoint,
                            params=geolocation_params).json()
except requests.exceptions.RequestException as e:
    print("Error getting geolocation data.")
    exit(1)


if len(response) > 0:
    weather_params = {"lat": response[0]["lat"], "lon": response[0]["lon"],
                      "units": "metric", "appid": api_key}
    try:
        weather_response = requests.get(
            weather_api_endpoint, params=weather_params).json()
    except requests.exceptions.RequestException as e:
        print("Error getting weather data.")
        exit(1)

    temperature = weather_response["main"]["temp"]
    feels_like = weather_response["main"]["feels_like"]
    max_temp = weather_response["main"]["temp_max"]
    min_temp = weather_response["main"]["temp_min"]
    name = weather_response["name"]
    sunrise = weather_response["sys"]["sunrise"]
    sunset = weather_response["sys"]["sunset"]
    # Convert Unix time to readable time
    sunrise = datetime.fromtimestamp(sunrise).strftime('%I:%M %p')
    sunset = datetime.fromtimestamp(sunset).strftime('%I:%M %p')

    print(
        "The temperature in {} is {}°C and it feels like {}°C".format(name, temperature, feels_like))
    print(
        "The maximum temperature is {}°C and the minimum temperature is {}°C".format(max_temp, min_temp))
    print("The sunrise is at {} and the sunset is at {}".format(sunrise, sunset))
else:
    print("Not able to find location. Please check the location and try again.")
