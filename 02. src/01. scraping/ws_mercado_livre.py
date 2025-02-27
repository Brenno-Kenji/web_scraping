# Importando módulos
import requests
import time
import re

from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def parse_html(response):
    soup = BeautifulSoup(response, 'html.parser')
    product_title = soup.find('h1', {'class': 'ui-pdp-title'}).text.strip()
    
    text_price = soup.find('span', {'class': 'andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact'}).text.strip().replace(',', '')
    number_price = re.findall(r'\d+', text_price)
    total_price = float(number_price[0]) / 100

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    return {
        'product_name': product_title,
        'price_whole': number_price[0][:-2],
        'price_fraction': number_price[0][2:],
        'total_price': total_price,
        'timestamp': timestamp
    }

if __name__ == '__main__':
    url = 'https://www.mercadolivre.com.br/barras-de-proteina-yopro-12-unidades-55g-whey-bar-nutrata-sabor-chocolate/p/MLB28747012#polycard_client=search-nordic&searchVariation=MLB28747012&wid=MLB3766013557&position=9&search_layout=grid&type=product&tracking_id=99e79a58-0a23-4bff-bcce-17f0705f2869&sid=search'
    response = get_html(url)
    ws = parse_html(response)
    print(ws)