import requests

boulder_url = "https://api.weather.gov/stations/KBDU/observations/latest"

def c_to_f(c):
    return (c * 9./5) + 32

def boulder_temp():
    response = requests.get(boulder_url)
    data = response.json()
    temp = data["properties"]["temperature"]["value"]
    return c_to_f(temp)