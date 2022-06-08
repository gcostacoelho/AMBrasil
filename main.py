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
from functions import funcUsers, funcOngs, funcADM

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

    while True:
        acao = int(input(Fore.RESET + '\t0-Fechar aplicativo\n\t1-Login usuário\n\t2-Login ONG\n\t3-Registrar\n\t4-Login ADM\n\n: '))
        
        if acao == 0: return 'sair'

        if acao == 1:
            while True:
                limpar()
                print(Fore.CYAN + '-------LOGIN-------' + Fore.RESET)
                user = input('Informe o seu CPF: ')
                valido = Usuario.search(user)            
                if valido: 
                    return 'comum'
                else: 
                    print(Fore.RED + 'Usuário não encontrado na base de dados')
                    sleep(3)
                    
        elif acao == 2:
            while True:
                limpar()
                print(Fore.CYAN + '-------LOGIN-------' + Fore.RESET)
                user = input('Informe o CNPJ da ONG: ')
                valido = Ong.search(user)
                if valido: return 'ong', valido
                else: 
                    print(Fore.RED + 'Ong não encontrada na base de dados')
                    sleep(3)
        
        elif acao == 3:
            while True:
                limpar()
                print('Registro de novo usuário')
                print(Fore.RED + 'AVISO: ' + Fore.RESET + "Para cadastros de ONG é necessário entrar em contato com nosso suporte")
                
                nome = input('Insira seu nome: ')
                email = input('Insira um email válido: ')
                cpf = input('Insira o seu CPF: ')
                sucesso = Usuario.insert(nome, email, cpf)
                if sucesso: break
                else: 
                    print('Algo deu errado, tente novamente')
                    sleep(3)
                    
        elif acao == 4:          
                    
                limpar()
                print(Fore.RED + 'PERFIL ADMINISTRADOR ')
                

                if sucesso: break
                else: 
                    print('Algo deu errado, tente novamente')
                    sleep(3)             
        else: 
            print("Não tenho essa opção por aqui... Por favor escolha apenas as que aparecem no menu")
            sleep(3)
            limpar()

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
        try:
            login = login()
            if login == 'sair': break
            
            elif login == 'comum':
                while True:
                    opcao = menuUser()
                    if opcao == 0: break
                    elif opcao == 1: funcUsers.inserir_denuncia()
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
                        funcOngs.visualizarCampanhas(login[1])
                        input("Pressione <ENTER> para continuar...")
                    elif opcao == 3:
                        funcOngs.atualizarCampanha(login[1])
                        input("Pressione <ENTER> para continuar...")
                    elif opcao == 4:
                        funcOngs.deletarCampanha(login[1])
                        input("Pressione <ENTER> para continuar...")
            else: break
        except: 
            print('Hmm, algo deu errado... Tente novamente mais tarde :(')
            input()
            break
        break
    
    print('Obrigado por usar o '+ Fore.GREEN + 'AMBrasil')