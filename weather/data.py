import requests
import bs4 

boulder_url = "https://api.weather.gov/stations/KBDU/observations/latest"

mcmurdo_url = "https://webmedia.antarcticanz.govt.nz/weather/sbweather.html"

def c_to_f(c):
    if c is None:
        return None
    return (c * 9./5) + 32

def boulder_temp():
    response = requests.get(boulder_url)
    data = response.json()
    temp = data["properties"]["temperature"]["value"]
    return c_to_f(temp)

def mcmurdo_temp():
    # yeah ok it's scott base, but that's what I can scrape
    try:
        response = requests.get(mcmurdo_url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        tstring = str(soup.find_all('td')[3].font.b.contents[0])
        temp = float(tstring.split("°")[0])
        return c_to_f(temp)
    except:
        return None