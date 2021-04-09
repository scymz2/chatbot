import requests
import json

api_key = "0123456789abcdef0123456789abcdef"
url = "http://api.openweathermap.org/data/2.5/weather?q=Ningbo,china&APPID=885aa9eb815b6b6b1b24ce7ade4b78d9"

res = requests.get(url)
data = res.json()
condition = data["main"]
temp = condition["temp"]
humidity = condition["humidity"]
pressure = condition["pressure"]

info = data["weather"]
des = info[0]
descrip = des["description"]


print("The current weather in Ningbo: " + str(descrip) + ", Temperature: " + str(temp-272.15) + "℃, Humidity: " + str(humidity) + "%, Pressure: " + str(pressure) + "p")
