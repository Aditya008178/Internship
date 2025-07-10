# Weather Reporter
# API: https://api.open-meteo.com/v1/forecast
# Goal: Input a city’s latitude/longitude → Get current temperature.
# If temp > 30°C → print “It’s hot!”
# If temp < 15°C → print “It’s cold!”

import requests

lat = float(input("Enter latitude: "))
lon = float(input("Enter longitude: "))

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
temp = response.json()["current_weather"]["temperature"]

print(f"Current temperature: {temp}°C")

if temp > 30:
    print("It's hot!")
elif temp < 15:
    print("It's cold!")


