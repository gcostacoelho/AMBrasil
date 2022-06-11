#Import resources
from time import sleep
import colorama
from colorama import Fore
#Import local files
from classes.desastres import Tipo_Desastre, Tipo_Local, Classificacao
from classes.func import *
from classes.users import Ong

colorama.init(autoreset='true')
BOLD = '\033[1m'

def inserirCampanha(ong):
    """Inserir Campanha"""
    print(f'Você está inserindo uma ' + Fore.RED + BOLD + 'Campanha' + Fore.RESET)

    Denuncia.view()
    while True:
        idDenuncia = int(input(Fore.RESET + '\nDentre essas denuncias, para qual é destinada as doações ' + Fore.RED + '(Digite apenas o número)' + Fore.RESET + ': '))
        valido = Denuncia.search(idDenuncia)
        if valido: break
        else: print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)

    Titulo = input('Titulo da Campanha ' + Fore.RED + '(Ex: Campanha da Fraternidade 2022)' + Fore.RESET + ': ')
    Descricao = input('Descricao da Campanha ' + Fore.RED + '(Ex: Sobre a Campanha)' + Fore.RESET + ': ')
    Meta = input('Descricao da Meta da Campanha ' + Fore.RED + '(Ex:Meta de Seguidores/Meta de arrecadação e ETC)' + Fore.RESET + ': ')
    Campanha_Doacao.insert(ong, Titulo, Descricao, idDenuncia, Meta)


def atualizarCampanha(ong):
    print(Fore.BLUE + '\n-------Atualizar Campanhas-------\n')
    
    Campanha_Doacao.search(ong, '', '', False)
    while True:
        idPostagem = input( Fore.RESET +'\n\nDigite o ID da campanha para selecionar: ')
        valido = Campanha_Doacao.search(ong, "", "", True)
        if valido: break
        else: print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)
    
    Denuncia.view()
    while True:
        idDenuncia = int(input(Fore.RESET + '\nDentre essas denuncias, para qual é destinada as doações ' + Fore.RED + '(Digite apenas o número)' + Fore.RESET + ': '))
        valido = Denuncia.search(idDenuncia)
        if valido: break
        else: print("Esse ID está" + Fore.RED + 'incorreto' + Fore.RESET + ", Por favor insira apenas o que aparece na lista")
        
    titulo = input('Titulo da Campanha ' + Fore.RED + '(Ex: Campanha da Fraternidade 2022)' + Fore.RESET + ': ')
    descricao = input('Descricao da Campanha ' + Fore.RED + '(Ex: Sobre a Campanha)' + Fore.RESET + ': ')
    meta = input('Descricao da Meta da Campanha ' + Fore.RED + '(Ex:Meta de Seguidores/Meta de arrecadação e ETC)' + Fore.RESET + ': ')

    Campanha_Doacao.update(ong, titulo, descricao, idDenuncia, meta, idPostagem)
    

def deletarCampanha(ong): 
    print(Fore.BLUE + '\n-------Deletar Campanhas-------\n\n\n')
    Campanha_Doacao.search(ong)

    idPostagem = input(Fore.RESET +'\n\nDigite o ID da campanha para excluir: ')
    confirmacao = input("Tem certeza que deseja " + Fore.RED + "excluir?" + Fore.RESET + "(s/n): ").lower()
    if confirmacao == 's': Campanha_Doacao.delete(idPostagem)
    else: return 0