import colorama
from colorama import Fore
from classes.users import Admin, Ong


colorama.init(autoreset='true')
BOLD = '\033[1m'



def verUsuarios():
    """View de todos os usuarios"""
    print(f'Você está vendo todos os usuarios cadastrados ' + Fore.RESET)
    print(25 * '-')
    Admin.view_all_users()
    
def delUsuario():
    print(f'Deletar Usuario ' + Fore.RESET)
    print(Fore.BLUE + '\n-------Deletar Campanhas-------\n\n\n')
    Admin.view_all_users()
    try:
        while True:
            UserId = Admin.search_user(id)
            break 
    except:
        print(Fore.RED + "Invalido" +Fore.RESET)
        pass   
    idUsuario = input( Fore.RESET +'\n\nDigite O id do Usuario para selecionar : ')
    Admin.delete_user(idUsuario)
    
def addOngs():
        print(Fore.GREEN+'Registro de nova Ong'+ Fore.RESET)
        print(Fore.RED + 'AVISO: ' + Fore.RESET + "Funcao exclusiva para Adminstradores")
        
        while True:
            nome = input('Insira nome da Ong: ')
            email = input('Insira um email válido: ')
            cnpj = input('Insira o cnpj: ')
            endereco = input('Insira o Endereco: ')
            tel = input('Insira o Telefone de contato: ')
            bio = input("Digite a Biogradia :")
            valido = Admin.insert_ong(nome, cnpj, endereco, email, tel, bio)
            if valido: break
            else :print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)
    
    
def verOngs():
    """View de todas as ongs"""
    print(f'Você está vendo todos as ongs cadastradas ' + Fore.RESET)
    print(25 * '-')
    Admin.view_all_ongs()
    
def delOng():
    print(f'Deletar Ong ' + Fore.RESET)
    print(Fore.BLUE + '\n-------Deletar Ong-------\n\n\n')
    Admin.view_all_ongs()
    try:
        while True:
            UserId = Admin.search_ong(id)
            break 
    except:
        print(Fore.RED + "Invalido" +Fore.RESET)
        pass   
    idOng = input( Fore.RESET +'\n\nDigite O id da Ong para selecionar : ')
    Admin.delete_ong(idOng)
    
def verCampanhas():
    print(f'Você está vendo todos as Campanhas cadastradas ' + Fore.RESET)
    print(25 * '-')
    Admin.view_all_campanha()

    
def verCampanha():
    print(f'Ver todas as Campanhas cadastradas de uma determinada Ong ' + Fore.RESET)
    print(25 * '-')
    while True:
        idong = (input(Fore.RESET + '\nqual o Id da Ong?: '))
        valido = Admin.serch_campanha(idong)
        if valido:
            Admin.view_campanha(idong)
            break
        else:
            print(Fore.RED + "Invalido")
            pass
    
def delCampanha():
    
    print(Fore.BLUE + '\n-------Deletar Campanhas-------\n\n\n')
    Admin.view_all_campanha()

    print(Fore.RED + "Invalido" +Fore.RESET) 
    idPostagem = input( Fore.RESET +'\n\nDigite O id da campanha para selecionar : ')
    Ong.delete(idPostagem)