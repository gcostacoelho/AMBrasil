#Import resources
from time import sleep
from turtle import update
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

    Tipo_Desastre.view()
    while True:
        denuncia = int(input(Fore.RESET + '\nDentre esses tipos de denuncias, qual é o que está envolvida ou englobada ' + Fore.RED + '(Digite apenas o número)' + Fore.RESET + ': '))
        valido = Tipo_Desastre.search(denuncia)
        if valido: break
        else: print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)

    Titulo = input('Titulo da Campanha ' + Fore.RED + '(Ex: Campanha da Fraternidade 2022)' + Fore.RESET + ': ')
    Descricao = input('Descricao da Campanha ' + Fore.RED + '(Ex: Sobre a Campanha)' + Fore.RESET + ': ')
    Meta = input('Descricao da Meta da Campanha ' + Fore.RED + '(Ex:Meta de Seguidores/Meta de arrecadação e ETC)' + Fore.RESET + ': ')
    Campanha_Doacao.insert(ong, Titulo, Descricao, denuncia, Meta)



def visualizarCampanhas(ong):
    print(Fore.BLUE + '\n-------Postagens/Campanhas-------\n')
    Campanha_Doacao.view()
    try:
        while True:
            valido = Ong.search(ong)
            break       
    except:
        print(Fore.RED + "Invalido")
        pass
    

def atualizarCampanha(ong):
    print(Fore.BLUE + '\n-------Atualizar Campanhas-------\n\n\n')
    Campanha_Doacao.view()
    try:
        while True:
            OngName = Ong.search(ong)
            break 
    except:
        print(Fore.RED + "Invalido")
        pass   
    idPostagem = input( Fore.RESET +'\n\nDigite O id da campanha para selecionar : ')
       
    Tipo_Desastre.view()
    while True:
        tipoDenuncia = int(input(Fore.RESET + '\nDentre esses tipos de denuncias, qual é o que está envolvida ou englobada ' + Fore.RED + '(Digite apenas o número)' + Fore.RESET + ': '))
        valido = Denuncia.search(tipoDenuncia)
        break
        
    Titulo = input('Titulo da Campanha ' + Fore.RED + '(Ex: Campanha da Fraternidade 2022)' + Fore.RESET + ': ')
    Descricao = input('Descricao da Campanha ' + Fore.RED + '(Ex: Sobre a Campanha)' + Fore.RESET + ': ')
    Meta = input('Descricao da Meta da Campanha ' + Fore.RED + '(Ex:Meta de Seguidores/Meta de arrecadação e ETC)' + Fore.RESET + ': ')

    Campanha_Doacao.update(ong, Titulo, Descricao, tipoDenuncia, Meta, idPostagem)
    

def deletarCampanha(ong): 
    
    print(Fore.BLUE + '\n-------Deletar Campanhas-------\n\n\n')
    Campanha_Doacao.view()
    try:
        while True:
            OngName = Ong.search(ong)
            break 
    except:
        print(Fore.RED + "Invalido" +Fore.RESET)
        pass   
    idPostagem = input( Fore.RESET +'\n\nDigite O id da campanha para selecionar : ')
    Campanha_Doacao.delete(idPostagem)