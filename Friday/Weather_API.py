import requests
from bs4 import BeautifulSoup as bs

def getWeather(search_term):
    url = "https://google.com/search?q= weather in" + search_term
    html = requests.get(url)
    data = bs(html.text, "html.parser")
    # for getting temperature
    temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text

    # for getting time and condition of sky
    sky = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
    res = sky.split('\n')
    time = res[0]
    sky = res[1]
    return temp,time,sky

