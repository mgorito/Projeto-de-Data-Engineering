import pandas as pd
import bancodados as bd

def carga_db(arquivo,user,password,database,host):
    """Função para escrever arquivo em base MySQL

    Arguments:
        arquivo arquivo com dados que irão persistir
        user usuário de conexão no banco
        password senha do usuário
        database database onde será criada a tabela para persistir os dados
        host host do banco de dados
    """
    df = pd.read_csv(arquivo,sep=";")
    if len(df) == 0:
        exit("arquivo vazio, não tem dados novos para carregar !")
    cursor = bd.bdados(database,user,password,host)
    cursor.escrever(df,"book")


if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()
    PATH = os.getenv("PATH_PROJETO")
    if os.path.isfile(os.path.join(PATH,"dados_limpos.csv")) == True:
        print("Os dados existem")
        carga_db(PATH+"dados_limpos.csv",os.getenv("USER_DB"),os.getenv("PASSWORD_DB"),os.getenv("DATABASE"),os.getenv("HOST_DB"))
      
    else:
        print("Não existe o arquivo.")
   