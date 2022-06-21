import re
from time import sleep
from colorama import Fore

def validRegex(info, type):
    if type == 'name':
        reg = re.compile('[A-z]')
        resp = reg.findall(info)
        if len(resp) > 1: 
            nomeV = ''.join(resp)
            return nomeV
        else: return False

    elif type == 'cpf':
        reg = re.compile('[0-9]')
        resp = reg.findall(info)
        if len(resp) == 11: 
            cpfV = ''.join(resp)
            return cpfV
        else: return False

    elif type == 'cnpj':
        reg = re.compile('[0-9]')
        resp = reg.findall(info)
        if len(resp) == 14: 
            cpfV = ''.join(resp)
            return cpfV
        else: return False

def validInput(input):
    if input == '':
        print(Fore.RED + "Por favor insira a informação corretamente" + Fore.RESET)
        sleep(2)
        return False
    else: return True