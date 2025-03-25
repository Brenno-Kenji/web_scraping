# Importando módulos
from scraping import *
from rules import *

# Arquivo principal
if __name__ == '__main__':
    # Realizando loop para leitura dos dados, baseado no arquivo de regras
    for key, value in products.items():
        # Realizando loop para leitura das URLs
        if key == 'Amazon':
            for url in value:
                scraper = WebScrapingAmazon(url)
                scraper.scrape()
                print(scraper)
        elif key == 'Mercado Livre':
            for url in value:
                scraper = WebScrapingMercadoLivre(url)
                scraper.scrape()
                print(scraper)
    