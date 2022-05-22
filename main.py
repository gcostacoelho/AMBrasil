#Import resources
from os import system
from time import sleep
import colorama
from colorama import Fore
#Import classes
from classes.desastres import Tipo_Desastre, Tipo_Local, Classificacao
from classes.users import Usuario, Ong


colorama.init(autoreset='true')
BOLD = '\033[1m'

def limpar():
    import os
    def limpar():
        if os.name == 'posix': _ = os.system('clear')
        else: _ = os.system('cls')
    sleep(1)
    limpar()


if __name__ == '__main__':
    limpar()
    print("main")