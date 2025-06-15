import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
params = {"q": city, "appid": API_KEY, "units": "metric"}

response = requests.get(BASE_URL, params=params)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Temperature in {city}: {temp}°C\nWeather: {desc}")
else:
    print("City not found.")
