# Importando módulos
import pandas as pd

from scraping import *
from rules import *

# Arquivo principal
if __name__ == '__main__':
    # Dicionário para armazenar todos os dados coletados
    raw_data = []

    # Realizando loop para leitura dos dados, baseado no arquivo de regras
    for key, value in products.items():
        # Selecionando a classe de scraping com base na chave
        if key == 'Amazon':
            scraper_class = WebScrapingAmazon
        elif key == 'Mercado Livre':
            scraper_class = WebScrapingMercadoLivre
        else:
            continue  # Ignorar chaves desconhecidas

        # Realizando loop para leitura das URLs
        for url in value:
            scraper = scraper_class(url)
            ws_data = scraper.scrape()
            ws_data['marketplace'] = key
            ws_data['url'] = url
            raw_data.append(ws_data)

    # Armazenando dados salvos em um arquivo .xlsx
    df = pd.DataFrame(raw_data)
    with pd.ExcelWriter('data/raw_data/scraping_data.xlsx', datetime_format='DD/MM/YYYY') as excel:
        df.to_excel(excel, sheet_name='scraping_data', index=False)