from bs4 import BeautifulSoup
import requests
import time
url = 'https://www.lazada.vn/products/adidas-originals-giay-superstar-nam-mau-trang-gz3413-i1809316659-s8144103383.html?mp=1&spm=a2o4n.seller.list.i40.10e034e6lKOEx6'


result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

prices = soup.find_all('div',{'id':'module_product_price_1'})[0].find('span').text
buy = soup.find_all('div',{'id':'module_add_to_cart'})[0].find('span').text
trangthai = ("Mua ngay")

if (buy == trangthai):
    print(url,buy)

if (buy != trangthai):
    while (True):
        if (buy != trangthai):
            print("...")
            time.sleep(2)



