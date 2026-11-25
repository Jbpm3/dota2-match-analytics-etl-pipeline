import requests
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 10.3157,
    "longitude": 123.8854,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": "Asia/Manila"
}

response = requests.get(url,params=params, timeout = 15)