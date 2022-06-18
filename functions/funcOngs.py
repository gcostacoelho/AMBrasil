#Import resources
from time import sleep
from typing import ChainMap
import colorama
from colorama import Fore

#Import local files
from classes.desastres import Tipo_Desastre, Tipo_Local, Classificacao
from classes.func import *
from classes.users import Ong
from valid import validInput

colorama.init(autoreset='true')
BOLD = '\033[1m'

def inserirCampanha(ong):
    print(f'Você está inserindo uma ' + Fore.BLUE + BOLD + 'Campanha' + Fore.RESET)

    Denuncia.view()
    while True:
        try:
            idDenuncia = int(input(Fore.RESET + '\nDentre essas denuncias, para qual é destinada as doações ' + Fore.RED + '(Digite apenas o número)' + Fore.RESET + ': '))
            valido = Denuncia.search(idDenuncia)
            if valido: break
            else: print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)
        except: print(Fore.RED + "Por favor, insira a opção corretamente" + Fore.RESET)
    
    while True:
        Titulo = input('Titulo da Campanha ' + Fore.RED + '(Ex: Campanha da Fraternidade 2022)' + Fore.RESET + ': ')
        TituloV = validInput(Titulo)
        if TituloV: break
    while True:
        Descricao = input('Descricao da Campanha ' + Fore.RED + '(Ex: Sobre a Campanha)' + Fore.RESET + ': ')
        descV = validInput(Descricao)
        if descV: break
    while True:
        Meta = input('Descricao da Meta da Campanha ' + Fore.RED + '(Ex:Meta de Seguidores/Meta de arrecadação e ETC)' + Fore.RESET + ': ')
        metaV = validInput(Meta)
        if metaV: break

    Campanha_Doacao.insert(ong, Titulo, Descricao, idDenuncia, Meta)


def atualizarCampanha(ong):
    print(Fore.BLUE + '\n-------Atualizar Campanhas-------\n')
    
    Campanha_Doacao.search('', '', ong)
    while True:
        try:
            idPostagem = int(input( Fore.RESET +'\n\nDigite o ID da campanha para selecionar: '))
            valido = Campanha_Doacao.search(idPostagem, '', ong, True)
            if valido: break
            else: print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)
        except: print(Fore.RED + "Por favor, insira a opção corretamente" + Fore.RESET)
    
    Denuncia.view()
    while True:
        try:
            idDenuncia = int(input(Fore.RESET + '\nDentre essas denuncias, para qual é destinada as doações ' + Fore.RED + '(Digite apenas o número)' + Fore.RESET + ': '))
            valido = Denuncia.search(idDenuncia)
            if valido: break
            else: print("Esse ID está " + Fore.RED + 'incorreto' + Fore.RESET + ", Por favor insira apenas o que aparece na lista")
        except: print(Fore.RED + "Por favor, insira a opção corretamente" + Fore.RESET)
    
    while True:
        titulo = input('Titulo da Campanha ' + Fore.RED + '(Ex: Campanha da Fraternidade 2022)' + Fore.RESET + ': ')
        TituloV = validInput(titulo)
        if TituloV: break
    while True:
        descricao = input('Descricao da Campanha ' + Fore.RED + '(Ex: Sobre a Campanha)' + Fore.RESET + ': ')
        descV = validInput(descricao)
        if descV: break
    while True:
        meta = input('Descricao da Meta da Campanha ' + Fore.RED + '(Ex:Meta de Seguidores/Meta de arrecadação e ETC)' + Fore.RESET + ': ')
        metaV = validInput(meta)
        if metaV: break

    Campanha_Doacao.update(ong, titulo, descricao, idDenuncia, meta, idPostagem)

def deletarCampanha(ong): 
    print(Fore.BLUE + '\n-------Deletar Campanhas-------\n\n\n')
    Campanha_Doacao.search("", "", ong)
    while True:
        try:
            idPostagem = int(input(Fore.RESET +'\nDigite o ID da campanha para excluir: '))
            valido = Campanha_Doacao.search(idPostagem, '', ong, True)
            
            if valido: 
                confirmacao = input("Tem certeza que deseja " + Fore.RED + "excluir?" + Fore.RESET + "(s/n): ").lower()
                if confirmacao == 's': 
                    Campanha_Doacao.delete(idPostagem)
                    break
            else: print(Fore.RED + 'Inválido... Insira apenas a opção certa' + Fore.RESET)
        except: print(Fore.RED + "Por favor, insira a opção corretamente" + Fore.RESET)