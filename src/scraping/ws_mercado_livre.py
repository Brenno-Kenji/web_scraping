# Importando módulos
import re

from scraping.web_scraping import *

# Classe para realizar o Web Scraping no site do Mercado Livre
class WebScrapingMercadoLivre(WebScraping):
    def extract_product_name(self) -> str:
        '''
        Método para extração do nome do produto
        '''
        return self.get_soup().find('h1', {'class': 'ui-pdp-title'}).text.strip()

    def extract_prices(self) -> list:
        '''
        Método para extração dos preços do produto
        '''
        price_text = self.get_soup().find('span', {'class': 'andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact'}).text.strip().replace('.', '')
        price_number = re.findall(r'\d+', price_text)

        price_whole = int(price_number[0])
        price_fraction = int(price_number[1]) if len(price_number) > 1 else 0
        price_total = float((price_whole + price_fraction) / 100)
        
        return [price_whole, price_fraction, price_total]

    def extract_seller_name(self) -> str:
        '''
        Método para extração do nome do vendedor
        '''
        raw_seller_name = self.get_soup().find('button', {'class': 'ui-pdp-seller__link-trigger-button non-selectable'}).text.strip()
        regex_seller_name = r'Vendido por(.*| .*)'
        seller_name = re.search(regex_seller_name, raw_seller_name).group(1).strip()
        
        return seller_name