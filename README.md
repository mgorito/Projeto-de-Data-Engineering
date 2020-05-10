# Projeto-de-Data-Engineering
Projeto para aprimorar habiliade de em pipeline de dados.
O projeto é divido em 3 scripts:
* scrapy.py -> script para fazer a raspagem de dados do site 'http://books.toscrape.com/'. 
* transformation.py -> script para tratar os dados brutos obtidos na raspagem. Responsável em fazer as transformações que permitirão persistir os dados no MySQL.
* carga -> inser os dados limpos no passo anterior e armazena em uma tablea MySQL.
