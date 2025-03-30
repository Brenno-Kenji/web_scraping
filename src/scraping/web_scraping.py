# Importando módulos
from abc import ABC, abstractmethod
from datetime import datetime
import requests
import pytz

from bs4 import BeautifulSoup

# Classe mãe para realização do Web Scraping
class WebScraping(ABC):
    def __init__(self, url: str):
        self.url = url
        self.__soup = None
        self.__data = {}

    def __parse_html(self):
        '''
        Método que realiza a requisição HTTP e lê o conteúdo HTML
        '''
        response = requests.get(self.url)
        if response.status_code == 200:
            self.__soup = BeautifulSoup(response.text, 'html.parser')
        else:
            raise Exception(f'Erro ao acessar {self.url}, Status Code: {response.status_code}')

    def get_soup(self):
        '''
        Método para obter o conteúdo HTML
        '''
        if self.__soup is None:
            self.__parse_html()
        return self.__soup

    @abstractmethod
    def extract_product_name(self):
        '''
        Método abstrato para extração dos nomes dos produtos
        '''
        pass

    @abstractmethod
    def extract_prices(self):
        '''
        Método abstrato para extração dos preços dos produtos
        '''
        pass

    @abstractmethod
    def extract_seller_name(self):
        '''
        Método abstrato para extração dos nomes de vendedores dos produtos
        '''
        pass

    def extract_timestamp(self):
        '''
        Método que extrai o momento da realização do script
        '''
        sao_paulo_tz = pytz.timezone('America/Sao_Paulo')
        return datetime.now(sao_paulo_tz).strftime('%Y-%m-%d %H:%M:%S')

    def scrape(self):
        '''
        Método que executa as extrações e retorna os dados em um dicionário
        '''
        self.__data = {
            'product_name': self.extract_product_name(),
            'price_whole': self.extract_prices()[0],
            'price_fraction': self.extract_prices()[1],
            'total_price': self.extract_prices()[2],
            'seller_name': self.extract_prices(),
            'timestamp': self.extract_timestamp()
        }
        return self.__data