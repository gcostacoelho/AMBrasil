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
    while True:
        try:
            cep = input(Fore.RESET + "Insira o CEP onde está acontecendo a denúncia: ")
            
            if len(cep) >= 8 and len(cep) <= 9: 
                dados = buscaCEP(cep)
                print(f'Cidade: {dados[1]}')
                print(f'Estado: {dados[0]}')
                print(f'Logradouro: {dados[2]}')
                
                while True:
                    correto = input('Os dados estão corretos (s/n): ').lower()
                    if correto == 's': 
                        idDenuncia=Denuncia.search("", denuncia)
                        Tipo_Local.insert(dados[0], dados[1], dados[2], cep, idDenuncia)
                        break                 
                    elif correto == 'n':
                        cep = input(Fore.RESET + 'Insira o CEP do local: ')
                        cidade = input('Insira o nome da cidade: ')
                        sigla = input('Insira a sigla do estado: ')
                        logradouro = input('Insira o logradouro: ')

                        idDenuncia=Denuncia.search("", denuncia)
                        Tipo_Local.insert(sigla, cidade, logradouro, cep, idDenuncia)
                        break
                    else: print('Por favor, digite apenas s - para "sim" ou n - para "não"')
            else: print(Fore.RED + 'O CEP inserido é inválido, tente novamente' + Fore.RESET)
        except: print('Algo deu errado :(')
        else: break