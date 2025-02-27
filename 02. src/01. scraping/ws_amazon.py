# Importando módulos
import requests
import time

from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def parse_html(response):
    soup = BeautifulSoup(response, 'html.parser')
    product_title = soup.find('span', {'id': 'productTitle'}).text.strip()
    price_whole = soup.find('span', {'class': 'a-price-whole'}).text.strip().replace(',', '')
    price_fraction = soup.find('span', {'class': 'a-price-fraction'}).text.strip().replace(',', '')
    total_price = float(price_whole + price_fraction) / 100
    seller_name = soup.find('a', {'id': 'sellerProfileTriggerId'}).text.strip()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    return {
        'product_name': product_title,
        'price_whole': price_whole,
        'price_fraction': price_fraction,
        'total_price': total_price,
        'seller_name': seller_name,
        'timestamp': timestamp
    }

if __name__ == '__main__':
    url = 'https://www.amazon.com.br/Whey-Grego-Bar-Caixa-12unid/dp/B09MDRH7G6/ref=sr_1_6?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2LJKND8IIINSP&dib=eyJ2IjoiMSJ9.BTGkWux7dUfwYoOBITp6flg0VqI2VSgQ7kbY1erkLZZRm3Dn9sORLhPFnWwfUE-lS2z3Esv--qyun3yyu7PGIhZv9u9KPMfGNf7AmXjfzEkch9qFpFiPmaawCMZNrzpLaE_VuR8YPODwHwKrISvtpgSg4Z21AyKwsZa590aTlxzArNn_pYUsvwP6fp843ty2MWq1zxZeOE4_by7wPqy_l8Jr3xim1f6TK18yWllL1HK8n99LVYN0h7Gk5s6-i6eN00vib1nmA3CqK9CmFuC8NoWFAaZF1eQ09ivt0PHjXeOBmBkzTf1OCoAnOlUVVOLeqx8Li3xFl0Z705JToU-Hl43J2eOxrWJTyqbsBIdQK28xpNMq7UY2WVv3lSRes-_YF1bF9L-2D8rjrzLpYz6u87rk1YAAdyDQ1rdY0F2WlSkNjFmsBoWW-b-k3K14uiH9.TAovBx1D-pz0Zgm0VpdFdIoQRnOTt9C_r2MBi50El6Q&dib_tag=se&keywords=nutrata&qid=1740236239&sprefix=nutrat%2Caps%2C255&sr=8-6&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9'
    response = get_html(url)
    ws = parse_html(response)
    print(ws)