import time

from bs4 import BeautifulSoup
import requests
import urllib.request

url = 'https://www.timeanddate.com/worldclock/vietnam/hanoi'

def THOI_GIAN():
    source = urllib.request.urlopen(url).read()
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    time = soup.find_all('span', {'class': 'h1'})[0].text
    date = soup.find_all('span', {'id': 'ctdat'})[0].text
    return time,date

while(True):
     print(THOI_GIAN())
     time.sleep(0.3)
