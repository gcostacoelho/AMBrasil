#Import resources
from sqlite3 import Error
from os import system
from time import sleep
import colorama
from colorama import Fore

#Import classes
from classes.desastres import Tipo_Desastre, Tipo_Local, Classificacao
from classes.func import Campanha_Doacao,Contato_Emerg, Denuncia
from classes.users import Usuario, Ong, Admin
from classes.conexao import Conexao
import schema

#Import functions
from functions import funcUsers, funcOngs
from functions import funcADM
from regexValid import valid
 
colorama.init(autoreset='true')
BOLD = '\033[1m'

###########################################################

def criar_conexao():
    """Criando a conexão com o banco de dados Sqlite3."""
    try:
        schema.initDB()
        #print(Fore.GREEN + "Tabelas criadas com sucesso")
    except Error as e:
        print(e)

###########################################################
def limpar():
    import os
    def limpar():
        if os.name == 'posix': _ = os.system('clear')
        else: _ = os.system('cls')
    sleep(1)
    limpar()

###########################################################
#Funções do programa
def login():
    limpar()

    print(Fore.GREEN + 25 * '-')
    print(BOLD + Fore.YELLOW + '--------' + Fore.GREEN + 'AMBRASIL' + Fore.YELLOW + '---------')
    print(Fore.GREEN + 25 * '-')
    print('\n')

    while True:
        try:
            acao = int(input(Fore.RESET + '\t0-Fechar aplicativo\n\t1-Login usuário\n\t2-Login ONG\n\t3-Registrar\n\t4-Login ADM\n: '))
            
            if acao == 0: return 'sair'

            if acao == 1:
                while True:
                    limpar()
                    print(Fore.CYAN + '-------LOGIN-------' + Fore.RESET)
                    user = input('Informe o seu CPF: ')
                    valido = Usuario.search(user)            
                    if valido: return 'comum'
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
                    while True:
                        nome = input('Insira seu nome: ')
                        nomeV = valid(nome,'name')
                        if nomeV: break
                        else: print(Fore.RED + 'Insira um nome válido' + Fore.RESET)

                    email = input('Insira um email válido: ')
                    
                    while True:
                        cpf = input('Insira o seu CPF: ')
                        cpfV = valid(cpf, 'cpf')
                        if cpfV: break
                        else: print(Fore.RED + 'Insira um CPF válido' + Fore.RESET)
                    sucesso = Usuario.insert(nomeV, email, cpfV)
                    if sucesso: break
                    else: 
                        print('Algo deu errado, tente novamente')
                        sleep(3)
                        
            elif acao == 4: 
                admin = 'adm'
                while True:
                    limpar()
                    print(Fore.CYAN + '-------LOGIN-------' + Fore.RESET)
                    logar = input('Login: ')
                    if admin == logar:
                        return 'adm'
                    else:  
                        print(Fore.RED + 'Incorreto')
                        sleep(2)
            else: 
                print(Fore.RED + "Não tenho essa opção disponível" + Fore.RESET)
                sleep(2)
                limpar()
        except:
            limpar()
            print(Fore.RED + 'Insira apenas os inputs das opções mostradas' + Fore.RESET)
            sleep(2)

###########################################################

def menuUser():
    limpar()
    print(Fore.GREEN + 25 * '-')
    print(BOLD + Fore.YELLOW + '--------' + Fore.GREEN + 'AMBRASIL' + Fore.YELLOW + '---------')
    print(Fore.GREEN + 25 * '-')
    
    while True:
        try:
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
        except:
            limpar()
            print(Fore.RED + 'Insira apenas os inputs das opções mostradas' + Fore.RESET)
            sleep(2)

###########################################################

def menuAdm():
    limpar()
    print(Fore.GREEN + 25 * '-')
    print(BOLD + Fore.YELLOW + '--------' + Fore.GREEN + 'AMBRASIL' + Fore.YELLOW + '---------')
    print(Fore.GREEN + 25 * '-')
    while True:
        try:
            print('O que você deseja fazer\n\n\t'+Fore.GREEN+'------------Usuario-----------'+Fore.RESET +'\n\t0-Sair\n\t1-Ver uma lista com todos os Usuarios cadastrados\n\t2-Deletar um usuario do Banco')
            print("\n\t"+Fore.GREEN+"------------Ong-----------"+Fore.RESET+"\n\t3-Cadastrar Ong no Sistema\n\t4-Ver uma lista com todos as Ongs cadastradas no Sistema\n\t5-Deletar uma Ong cadastrada no Sistema")
            print("\n\t"+Fore.GREEN+"------------Campanha-----------"+Fore.RESET+"\n\t6-Visualizar Campanhas no Sistema\n\t7-Visualizar Campanhas de uma determinada Ong no Sistema\n\t8-Deletar uma Campanha cadastrada no Sistema")
            print("\n\t"+Fore.GREEN+"------------Triagem-----------"+Fore.RESET+"\n\t9-Ver Denuncias\n\t10-Fazer triagem de Denuncias ")
            
            op = int(input("\t: "))
            if op == 0: return op
            elif op == 1: return op
            elif op == 2: return op
            elif op == 3: return op
            elif op == 4: return op
            elif op == 5: return op
            elif op == 6: return op
            elif op == 7: return op
            elif op == 8: return op
            elif op == 9: return op
            elif op == 10: return op
            else:
                print(Fore.RED + 'Não tenho essa opção disponível')
                print(BOLD + 'Por favor selecione apenas as que aparecem no menu')
                sleep(2)
                limpar()
        except: 
            limpar()
            print(Fore.RED + 'Insira apenas os inputs das opções mostradas' + Fore.RESET)
            sleep(2)

###########################################################

def menuOng():
    limpar()
    print(Fore.GREEN + 25 * '-')
    print(BOLD + Fore.YELLOW + '--------' + Fore.GREEN + 'AMBRASIL' + Fore.YELLOW + '---------')
    print(Fore.GREEN + 25 * '-')
    
    while True:
        try:
            op = int(input("O que você deseja fazer\n\t0-Sair\n\t1-Registrar nova campanha\n\t2-Ver campanhas de doação\n\t3-Ver minhas campanhas\n\t4-Atualizar uma campanha\n\t5-Excluir uma campanha\n"))
            if op == 0: return op
            elif op == 1: return op
            elif op == 2: return op
            elif op == 3: return op
            elif op == 4: return op
            elif op == 5: return op
            elif op == 6: return op
            elif op == 7: return op
            else:
                print(Fore.RED + 'Não tenho essa opção disponível')
                print(BOLD + 'Por favor selecione apenas as que aparecem no menu')
                sleep(2)
                limpar()       
        except:
            limpar()
            print(Fore.RED + 'Insira apenas os inputs das opções mostradas' + Fore.RESET)
            sleep(2)

###########################################################

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
                elif opcao == 1: funcUsers.inserir_denuncia()
                elif opcao == 2: Campanha_Doacao.view()
                elif opcao == 3: Contato_Emerg.view()

        elif login == 'adm':
            while True:
                opcao = menuAdm()
                if opcao == 0: break
                elif opcao == 1: Usuario.view()
                elif opcao == 2: funcADM.delUsuario()

                elif opcao == 3: funcADM.addOngs()
                elif opcao == 4: Ong.view()
                elif opcao == 5: funcADM.delOng()

                elif opcao == 6: Campanha_Doacao.view()
                elif opcao == 7: funcADM.verCampanha_ong()
                elif opcao == 8: funcADM.delCampanha()

                elif opcao == 9:  Denuncia.view()
                elif opcao == 10: funcADM.updateDenuncia()     

        elif login[0] == 'ong':
            while True:
                opcao = menuOng()

                if opcao == 0: break
                elif opcao == 1: funcOngs.inserirCampanha(login[1])
                elif opcao == 2: 
                    limpar()
                    print(Fore.BLUE + '\n-------Campanhas de doação-------\n')                   
                    Campanha_Doacao.view()
                elif opcao == 3: 
                    limpar()
                    print(Fore.BLUE + '\n-------Minhas campanhas-------\n')
                    Campanha_Doacao.search('', '', login[1])
                elif opcao == 4: funcOngs.atualizarCampanha(login[1])
                elif opcao == 5: funcOngs.deletarCampanha(login[1]) 
        break
    
    print('Obrigado por usar o '+ Fore.GREEN + 'AMBrasil')