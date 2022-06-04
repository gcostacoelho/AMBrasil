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
        denuncia = int(input(Fore.RESET + '\nDentre esses tipos de denuncias, qual é o que está envolvida ou englobada ' + Fore.RED + '(Digite apenas o número)' + Fore.RESET + ': '))
        valido = Denuncia.search(denuncia)
        if valido: break
        else: print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)

    Titulo = input('Titulo da Campanha ' + Fore.RED + '(Ex: Campanha da Fraternidade 2022)' + Fore.RESET + ': ')
    Descricao = input('Descricao da Campanha ' + Fore.RED + '(Ex: Sobre a Campanha)' + Fore.RESET + ': ')
    Meta = input('Descricao da Meta da Campanha ' + Fore.RED + '(Ex:Meta de Seguidores/Meta de arrecadação e ETC)' + Fore.RESET + ': ')


    Campanha_Doacao.insert(ong, Titulo, Descricao, denuncia, Meta)



def visualizarCampanhas():
    print('visualizarCampanhas')


def atualizarCampanha():
    print('atualizar')

def deletarCampanha():
    print('deletarCampanha')