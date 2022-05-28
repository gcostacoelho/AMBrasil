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
        #print(Fore.GREEN + "Tabelas criadas com sucesso")
    except Error as e:
        print(e)

def limpar():
    import os
    def limpar():
        if os.name == 'posix': _ = os.system('clear')
        else: _ = os.system('cls')
    sleep(1)
    limpar()

def menu():
    def cabecalho():
        print(Fore.GREEN + 25 * '_')
        print(BOLD + Fore.YELLOW + '--------' + Fore.GREEN + 'AMBRASIL' + Fore.YELLOW + '---------')
        print(Fore.GREEN + 25 * '-')

    def user():
        limpar()
        print('Bem vindo usuário')
        while True:
            op = int(input("O que você deseja fazer\n\t0-Sair\n\t1-Registrar denúncia\n\t2-Ver campanhas de doação\n"))
            if op == 0: break
            elif op == 1: 
                print('Chama inserir denúncia')
                break
            elif op == 2:
                print('Chama view de campanhas')
                break
            else:
                print(Fore.RED + 'Não tenho essa opção disponível')
                print(BOLD + 'Por favor selecione apenas as que aparecem no menu')
                sleep(2)
                limpar()

    def ong():
        limpar()
        print('Bem vindo ONG')
        while True:
            op = int(input("O que você deseja fazer\n\t0-Sair\n\t1-Registrar nova campanha\n\t2-Ver campanhas de doação\n"))
            if op == 0: break
            elif op == 1: 
                print('Chama inserir campanha')
                break
            elif op == 2:
                print('Chama view de campanhas')
                break
            else:
                print(Fore.RED + 'Não tenho essa opção disponível')
                print(BOLD + 'Por favor selecione apenas as que aparecem no menu')
                sleep(2)
                limpar()

    limpar()
    cabecalho()
    sleep(3)
    limpar()
    print(Fore.CYAN + BOLD + '-----------Login------------')
    tipo = int(input('Informe o seu tipo de usuário\n\n\t0-Fechar aplicativo\n\t1-Usuário comum\n\t2-ONG\n'))

    if tipo == 0: print('Até logo')
    elif tipo==1: user()
    elif tipo == 2: ong()
    

if __name__ == '__main__':
    criar_conexao()
    menu()

    