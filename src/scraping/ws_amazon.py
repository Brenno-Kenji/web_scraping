# Importando módulos
from scraping.web_scraping import *

# Classe para realizar o Web Scraping no site da Amazon
class WebScrapingAmazon(WebScraping):
    def extract_product_name(self) -> str:
        '''
        Método para extração do nome do produto
        '''
        return self.get_soup().find('span', {'id': 'productTitle'}).text.strip()

    def extract_prices(self) -> list:
        '''
        Método para extração dos preços do produto
        '''
        price_whole = self.get_soup().find('span', {'class': 'a-price-whole'}).text.strip().replace(',', '').replace('.', '')
        price_fraction = self.get_soup().find('span', {'class': 'a-price-fraction'}).text.strip().replace(',', '').replace('.', '')

        price_total = float((price_whole + price_fraction)) / 100 if float(price_fraction) > 0 else float(price_whole)
        
        return [float(price_whole), float(price_fraction), price_total]

    def extract_seller_name(self) -> str:
        '''
        Método para extração do nome do vendedor
        '''
        bs_seller_name = self.get_soup().find('a', {'id': 'sellerProfileTriggerId'})
        
        return bs_seller_name.text.strip() if bs_seller_name != None else 'Amazon.com.br'