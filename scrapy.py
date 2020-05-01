from bs4 import BeautifulSoup
import requests
import pandas as pd

#fazendo o request na pagina
url_base = 'http://books.toscrape.com/'
page = requests.get(url_base)

#verificando se a url_base está de pé
if  page.status_code == 200:
    print("site está de pé.")
else:
    exit("site está fora do ar.")
    
#criando um objeto bs4 
soup = BeautifulSoup(page.content,'html.parser')
result = soup.find(id='default')
lista_sites = []
for link in result.find_all('a',href=True):
    #print("link obtido {}".format(link['href']))
    if "category" in link['href']:
        lista_sites.append(link['href'])

#retirando o primeiro link e criando o df que vamos usar par criar os dados
lista_sites.pop(0)
#acessando as categorias do site
dic_link = []
for l in lista_sites:
    url_categoria = url_base+l
    # print(url_categoria)
    page_categoria = requests.get(url_categoria)
    soup_link = BeautifulSoup(page_categoria.content,'html.parser')
    result_link = soup_link.find_all('article')
    for a in result_link:
        d = {
        "nome": a.find('h3').text,
        "categoria": soup_link.find('div',class_='page-header action').text,
        "qnt_estrela": a.find('p')['class'][len(a.find('p')['class'])-1],
        "preco": a.find('p', class_= "price_color").text,
        "estoque": a.find('p', class_= "instock availability").text
        }
        dic_link.append(d)
      
df_links = pd.DataFrame.from_dict(dic_link)
