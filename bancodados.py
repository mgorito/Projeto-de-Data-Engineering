import pandas as pd
from sqlalchemy import create_engine

class bdados():
    """Classe para escrever em banco de dados"""

    """Atributos: conexao: conexao com banco de dados"""

    def __init__(self,database,user,pwd,host):

        """Retorna um objeto banco de dados com a conexao ja definida"""
        self.engine = create_engine("mysql://"+user+":"+pwd+"@"+host+"/"+database+"",echo = False)

    def leitura(self,query):
        """Lê dataframe do banco de dados """
        return  pd.read_sql(query,self.engine)

    def escrever(self,df,tabela):
        """Grava dataframe no banco de dados """
        try:
            df.to_sql(tabela, con = self.engine,if_exists='append',index=False)
            print("Dados persistidos com sucesso!")
        except:
            print('Não existe ou não foi possível completar a conexão.')
           



   