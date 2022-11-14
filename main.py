import time

from bs4 import BeautifulSoup
import requests
import urllib.request

url = 'https://www.lazada.vn//products/i1240264949-s4621963744.html'

def LAZ():
    source = urllib.request.urlopen(url).read()
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    prices = soup.find_all('span', {'class': 'pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl'})[0].text
    buy = soup.find_all('span', {'class': 'pdp-button-text'})[0].text
    return prices,buy

while(True):
     print(LAZ(),url)
     time.sleep(1)
