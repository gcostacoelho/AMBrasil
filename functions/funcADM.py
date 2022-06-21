from time import sleep
import colorama
from colorama import Fore
from classes.func import Denuncia, Campanha_Doacao 
from classes.users import Admin, Ong, Usuario
from valid import validRegex, validInput

colorama.init(autoreset='true')
BOLD = '\033[1m'
    
def delUsuario():
    print(Fore.BLUE + '\n-------Deletar Usuario-------\n\n\n')
    Usuario.view()
 
    while True:
        idUsuario = input( Fore.RESET +'\n\nDigite o id do Usuario para selecionar : ')
        verdade = Usuario.search("", idUsuario)
        if verdade:
            Usuario.delete(idUsuario)
            break
        else: 
            print(Fore.RED + "Invalido" +Fore.RESET)
            pass
    
def addOngs():
    print(Fore.GREEN+'Registro de nova Ong'+ Fore.RESET)
    print(Fore.RED + 'AVISO: ' + Fore.RESET + "Funcao exclusiva para Adminstradores")
    while True:
        try:
            while True:
                nome = input('Insira nome da Ong: ')
                nomeV = validRegex(nome,'name')
                if nomeV: break
                else: print(Fore.RED + 'Insira um nome válido' + Fore.RESET)
            
            while True:
                cnpj = input('Insira o cnpj: ')
                cnpjV = validRegex(cnpj, 'cnpj')
                if cnpjV: break
                else: print(Fore.RED + 'Insira um CNPJ válido' + Fore.RESET)
            
            while True:
                email = input('Insira um email válido: ')
                emailV = validInput(email)
                if emailV: break
            
            while True:
                endereco = input('Insira o Endereco: ')
                enderecoV = validInput(endereco)
                if enderecoV: break

            while True:
                tel = input('Insira o Telefone de contato: ')
                telV = validInput(tel)
                if telV: break

            while True:
                bio = input("Digite a Biografia :")
                bioV = validInput(bio)
                if bioV: break
        except:
            print('Aconteceu algo de errado, por favor tente novamente')
            sleep(2)
        else:
            Ong.insert(nomeV, cnpjV, endereco, email, tel, bio)
            break

def delOng():
    print(f'Deletar Ong ' + Fore.RESET)
    print(Fore.BLUE + '\n-------Deletar Ong-------\n\n\n')
    Ong.view()
    try:
        while True:
            idOng = input( Fore.RESET +'\n\nDigite o id da Ong para selecionar: ')
            valido = Ong.search('', idOng)
            if valido:
                Ong.delete(idOng)
                break
    except:
        print(Fore.RED + "Invalido" +Fore.RESET)
        pass
    
def verCampanha_ong():
    print(f'Ver todas as Campanhas cadastradas de uma determinada Ong ' + Fore.RESET)
    print(25 * '-')
    while True:
        idOng = (input(Fore.RESET + '\nqual o Id da Ong?: '))
        valido = Admin.serch_campanha(idOng)
        if valido:
            Campanha_Doacao.search("", "", idOng)
            break
        else:
            print(Fore.RED + "Invalido")
            pass

def delCampanha():
    print(Fore.BLUE + '\n-------Deletar Campanhas-------\n\n\n')
    Campanha_Doacao.view()
    while True:
        idPostagem = input( Fore.RESET +'\n\nDigite o id da campanha para selecionar: ')
        idOng = input( Fore.RESET +'Digite o id da Ong : ')
        valido = Campanha_Doacao.search(idPostagem, "", idOng, True)
        if valido:
            Campanha_Doacao.delete(idPostagem) 
            break
        else:
            print("\ninvalido")

def updateDenuncia():
    print(f'Você está vendo todos as Denuncias ' + Fore.RESET)
    print(25 * '-')
    Denuncia.view()
    while True:
        idenuncia = input( Fore.RESET +'\n\nDigite o id do Usuario para selecionar : ')
        verdade = Denuncia.search(idenuncia)
        if verdade: 
            situacao = input( Fore.RESET +'\n\nDigite a situacao da Denuncia selecionada: ')
            Admin.update_denuncia(situacao, idenuncia)
            break
        else:
            print(Fore.RED + "ID Invalido" +Fore.RESET)
            pass