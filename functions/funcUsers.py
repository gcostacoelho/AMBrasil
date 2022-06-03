#Import resources
from time import sleep
import colorama
from colorama import Fore
#Import local files
from classes.desastres import Tipo_Desastre, Tipo_Local, Classificacao
from classes.func import Denuncia
from main import limpar
from Api.request import buscaCEP

colorama.init(autoreset='true')
BOLD = '\033[1m'



def inserir_denuncia():
    limpar()
    """Inserir denúncia"""
    print(f'Você está inserindo uma ' + Fore.RED + BOLD + 'denúncia' + Fore.RESET)
    print(25 * '-')
    denuncia = input('Nome da denúncia ' + Fore.RED + '(Ex: Enchente no centro da cidade)' + Fore.RESET + ': ')
    
    contato = input('Insira um telefone para um possível contato: ')
    
    Tipo_Desastre.view()
    while True:
        tipoDesastre = int(input(Fore.RESET + '\nDentre esses tipos de desastres, qual é o que está ocorrendo ' + Fore.RED + '(Digite apenas o número)' + Fore.RESET + ': '))
        valido = Tipo_Desastre.search(tipoDesastre)
        if valido: break
        else: print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)
    
    Classificacao.view()
    while True:
        classificacao = int(input(Fore.RESET + '\nDentre as classificações mostradas, qual está ocorrendo ' + Fore.RED + '(Digite apenas o número)' + Fore.RESET + ': '))
        valido = Classificacao.search(classificacao)
        if valido: break
        else:  print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)

    Denuncia.insert(denuncia, contato, tipoDesastre, classificacao)

    limpar()

    """Inserir local"""
    print(buscaCEP('07747270'))

    

