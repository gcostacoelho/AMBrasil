import colorama
from colorama import Fore
from classes.func import Denuncia, Campanha_Doacao 
from classes.users import Admin, Ong

colorama.init(autoreset='true')
BOLD = '\033[1m'

def verUsuarios():
    """View de todos os usuarios"""
    print(f'Você está vendo todos os usuarios cadastrados ' + Fore.RESET)
    print(25 * '-')
    Admin.view_all_users()


def update_usuario():
    print(f'Você está vendo todos os usuarios ' + Fore.RESET)
    print(25 * '-')
    Admin.view_all_users()
    while True:
        iduser = input( Fore.RESET +'\n\nDigite O id do Usuario para selecionar : ')
        verdade = Admin.search_user(iduser)
        if verdade :  break
        else: 
            print(Fore.RED + "ID Invalido" +Fore.RESET)
            pass
    nome = input( Fore.RESET +'\n\nDigite O o nome do Usuario : ')
    email = input( Fore.RESET +'\n\nDigite O email do Usuario : ')
    cpf = input( Fore.RESET +'\n\nDigite O CPF do Usuario : ')

    Admin.update_user(nome, email, cpf,iduser)

    
def delUsuario():
    print(Fore.BLUE + '\n-------Deletar Usuario-------\n\n\n')
    Admin.view_all_users()
 
    while True:
        idUsuario = input( Fore.RESET +'\n\nDigite O id do Usuario para selecionar : ')
        verdade = Admin.search_user(idUsuario)
        if verdade :  break
        else: 
            print(Fore.RED + "Invalido" +Fore.RESET)
            pass 
    Admin.delete_user(idUsuario)
    
def addOngs():
        print(Fore.GREEN+'Registro de nova Ong'+ Fore.RESET)
        print(Fore.RED + 'AVISO: ' + Fore.RESET + "Funcao exclusiva para Adminstradores")
        
        nome = input('Insira nome da Ong: ')
        email = input('Insira um email válido: ')
        cnpj = input('Insira o cnpj: ')
        endereco = input('Insira o Endereco: ')
        tel = input('Insira o Telefone de contato: ')
        bio = input("Digite a Biogradia :")
        Admin.insert_ong(nome, cnpj, endereco, email, tel, bio)

    
    
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

    
def verCampanha_ong():
    print(f'Ver todas as Campanhas cadastradas de uma determinada Ong ' + Fore.RESET)
    print(25 * '-')
    while True:
        idong = (input(Fore.RESET + '\nqual o Id da Ong?: '))
        valido = Admin.serch_campanha(idong)
        if valido:
            Campanha_Doacao.search("","",idong)
            break
        else:
            print(Fore.RED + "Invalido")
            pass

    
def delCampanha():
    print(Fore.BLUE + '\n-------Deletar Campanhas-------\n\n\n')
    Admin.view_all_campanha()
    while True:
        idPostagem = input( Fore.RESET +'\n\nDigite O id da campanha para selecionar : ')
        idOng = input( Fore.RESET +'\n\nDigite O id da Ong : ')
        valido = Campanha_Doacao.search(idPostagem,"",idOng,True)
        if valido:
            Campanha_Doacao.delete(idPostagem) 
            break

        else:
            print("\ninvalido")





def verDenuncia():
    print(f'Você está vendo todas as Denuncias ' + Fore.RESET)
    print(25 * '-')
    Denuncia.view()



def updateDenuncia():
    print(f'Você está vendo todos as Denuncias ' + Fore.RESET)
    print(25 * '-')
    Denuncia.view()
    while True:
        idenuncia = input( Fore.RESET +'\n\nDigite O id do Usuario para selecionar : ')
        verdade = Admin.search_denuncia(idenuncia)
        situacao = input( Fore.RESET +'\n\nDigite a situacao da Denuncia selecionada  : ')
        if verdade :  break
        else: 
            print(Fore.RED + "ID Invalido" +Fore.RESET)
            pass
        
    Admin.update_denuncia(situacao,idenuncia)
