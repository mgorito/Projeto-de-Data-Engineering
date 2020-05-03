import os
import pandas as pd
from dotenv import load_dotenv

def carregar_dados(f):
   df =  pd.read_csv(f,sep=";")
   df["categoria"] =  df.apply(lambda x: categoria(x["categoria"]),axis=1)
   df["preco"] = df.apply(lambda x: preco(x["preco"]),axis=1)
   df["qnt_estrela"] = df.apply(lambda x: qnt_estrela(x["qnt_estrela"]),axis=1)
   df["estoque"] = df.apply(lambda x: estoque(x["estoque"]),axis=1)
   return df

def categoria(row):
    return row.strip('\n')

def estoque(row):
    return row.strip('\n\n \n')

def preco(row):
    return float(row.strip('£'))

def qnt_estrela(row):
    dic = {
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5
    }
    if dic.get(row):
        return dic.get(row)
    else: 
        return 0
    


if __name__ == "__main__":
    #carregando as variaveis de ambiente
    load_dotenv()
    PATH = os.getenv("PATH_PROJETO")
    if os.path.isfile(os.path.join(PATH,"dados_brutos.csv")) == True:
        print("Os dados existem")
        dados = carregar_dados(PATH+"dados_brutos.csv")
        dados.to_csv(PATH+"dados_limpos.csv",sep=";",index=False)
    else:
        print("Não existe o arquivo.")
   