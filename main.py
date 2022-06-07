#Import resources
from sqlite3 import Error
from os import system
from time import sleep
import colorama
from colorama import Fore

#Import classes
from classes.desastres import Tipo_Desastre, Tipo_Local, Classificacao
from classes.func import Campanha_Doacao,Contato_Emerg
from classes.users import Usuario, Ong
from classes.conexao import Conexao
import schema

#Import functions
from functions import funcUsers, funcOngs


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

#Funções do programa
def login():
    limpar()

    print(Fore.GREEN + 25 * '-')
    print(BOLD + Fore.YELLOW + '--------' + Fore.GREEN + 'AMBRASIL' + Fore.YELLOW + '---------')
    print(Fore.GREEN + 25 * '-')
    print('\n')

    print(Fore.CYAN + BOLD + '-----------Login------------')
    tipo = int(input('Informe o seu tipo de usuário\n\n\t0-Fechar aplicativo\n\t1-Usuário comum\n\t2-ONG\n'))
    
    if tipo == 0: return 'sair'

    if tipo == 1:
        while True:
            limpar()
            user = input('Informe o seu CPF: ')
            valido = Usuario.search(user)            
            if valido: 
                return 'comum'
            else: 
                print(Fore.RED + 'Usuário não encontrado na base de dados')
                input()
                
    elif tipo == 2:
        while True:
            limpar()
            user = input('Informe o CNPJ da ONG: ')
            valido = Ong.search(user)
            if valido: return 'ong', valido
            else: 
                print(Fore.RED + 'Ong não encontrada na base de dados')
                input()

def menuUser():
    limpar()
    print(Fore.GREEN + 25 * '-')
    print(BOLD + Fore.YELLOW + '--------' + Fore.GREEN + 'AMBRASIL' + Fore.YELLOW + '---------')
    print(Fore.GREEN + 25 * '-')
    
    while True:
        op = int(input("O que você deseja fazer\n\t0-Sair\n\t1-Registrar denúncia\n\t2-Ver campanhas de doação\n\t3-Ver contatos de emergência\n"))
        if op == 0: return op
        elif op == 1: return op
        elif op == 2: return op
        elif op == 3: return op
        else:
            print(Fore.RED + 'Não tenho essa opção disponível')
            print(BOLD + 'Por favor selecione apenas as que aparecem no menu')
            sleep(2)
            limpar()

def menuOng():
    limpar()
    print(Fore.GREEN + 25 * '-')
    print(BOLD + Fore.YELLOW + '--------' + Fore.GREEN + 'AMBRASIL' + Fore.YELLOW + '---------')
    print(Fore.GREEN + 25 * '-')
    
    while True:
        op = int(input("O que você deseja fazer\n\t0-Sair\n\t1-Registrar nova campanha\n\t2-Ver campanhas de doação\n\t3-Atualizar uma campanha\n\t4-Excluir uma campanha\n"))
        if op == 0: return op
        elif op == 1: return op
        elif op == 2: return op
        elif op == 3: return op
        elif op == 4: return op
        else:
            print(Fore.RED + 'Não tenho essa opção disponível')
            print(BOLD + 'Por favor selecione apenas as que aparecem no menu')
            sleep(2)
            limpar()

if __name__ == '__main__':
    criar_conexao()
    limpar()
    print(Fore.GREEN + 25 * '-')
    print(BOLD + Fore.YELLOW + '--------' + Fore.GREEN + 'AMBRASIL' + Fore.YELLOW + '---------')
    print(Fore.GREEN + 25 * '-')
    sleep(3)

    while True:
        login = login()
        if login == 'sair': break
        
        elif login == 'comum':
            while True:
                opcao = menuUser()
                if opcao == 0: break
                elif opcao == 1:
                    funcUsers.inserir_denuncia()
                    input("Pressione <ENTER> para continuar...")
                elif opcao == 2: Campanha_Doacao.view()
                elif opcao == 3: Contato_Emerg.view()

        elif login[0] == 'ong':
            while True:
                opcao = menuOng()
                if opcao == 0: break
                elif opcao == 1: 
                    funcOngs.inserirCampanha(login[1])
                    input("Pressione <ENTER> para continuar...")
                elif opcao == 2: 
                    print('Chama view de campanhas')
                    input("Pressione <ENTER> para continuar...")
                elif opcao == 3:
                    print('Chama atualizar campanhas')
                    input("Pressione <ENTER> para continuar...")
                elif opcao == 4:
                    print('Chama view de campanhas')
                    input("Pressione <ENTER> para continuar...")
        break
    
    print('Obrigado por usar o '+ Fore.GREEN + 'AMBrasil')




    