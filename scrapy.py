from bs4 import BeautifulSoup
import requests

#criando objeto beautifulsoup
def create_link(l):
    url_categoria = url_base+l
    page_categoria = requests.get(url_categoria)
    if  page_categoria.status_code == 200:
        print("página está de pé.")
    else:
        exit("página está fora do ar.")
    return BeautifulSoup(page_categoria.content,'html.parser')

#função teste para multiplas páginas
def test_pages(pg):
    if pg.find('li',class_="next"):
            return True 
    return False    

#coletando as informações da pagina
def get_link_data(soup_obj,dic_link):
    result_link = soup_obj.find_all('article',class_='product_pod')
    for a in result_link:
        d = {
        "nome": a.find('h3').text,
        "categoria": soup_obj.find('div',class_='page-header action').text,
        "qnt_estrela": a.find('p')['class'][len(a.find('p')['class'])-1],
        "preco": a.find('p', class_= "price_color").text,
        "estoque": a.find('p', class_= "instock availability").text
        }
        dic_link.append(d)
    return dic_link

#acessando as informações da pagina
def scrap_data(l,dic_link):
    soup_link = create_link(l)
    count = 1
    print("Página: {}".format(count))
    dic_link = get_link_data(soup_link,dic_link)
    if test_pages(soup_link) == True:
        link_referencia = soup_link.find('li',class_="next").a.get('href')
        next_page = create_link(l[:l.rfind('/')+1]+link_referencia)
        while test_pages(next_page)==True:
            count+=1
            print("Link "+l[:l.rfind('/')+1]+link_referencia)
            print("Página: {}".format(count))
            dic_link = get_link_data(next_page,dic_link)
            try:
                link_referencia = next_page.find('li',class_="next").a.get('href')
            except AttributeError :
                break
            next_page = create_link(l[:l.rfind('/')+1]+link_referencia)
        return dic_link      
    else:
        return dic_link

 
if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    import pandas as pd
    load_dotenv()
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
    lista_sites = [link['href'] for link in result.find_all('a',href=True) if "category" in link['href'] ]
    #retirando o primeiro link e criando o df que vamos usar par criar os dados
    lista_sites.pop(0)
    dic_data = []
    count_link  = 1
    #acessando as categorias do site
    for l in lista_sites:
        print('Link para categoria {}'.format(count_link))
        dic_data = scrap_data(l,dic_data)
        count_link +=1
    #transformando em dataframe para facilitar armazenamento relacional
    df_links = pd.DataFrame.from_dict(dic_data)
    df_links.to_csv(os.getenv("OUTPUT_PATH")+"dados_brutos.csv",sep=";",index=False)
