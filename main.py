#Import resources
from sqlite3 import Error
from os import system
from time import sleep
import colorama
from colorama import Fore
#Import classes
from classes.desastres import Tipo_Desastre, Tipo_Local, Classificacao
from classes.users import Usuario, Ong
import schema


colorama.init(autoreset='true')
BOLD = '\033[1m'

def criar_conexao():
    """Criando a conexão com o banco de dados Sqlite3."""
    try:
        schema.initDB()
        print(Fore.GREEN + "Tabelas criadas com sucesso")
    except Error as e:
        print(e)


def limpar():
    import os
    def limpar():
        if os.name == 'posix': _ = os.system('clear')
        else: _ = os.system('cls')
    sleep(1)
    limpar()


if __name__ == '__main__':
    limpar()
    criar_conexao()
    print("main")