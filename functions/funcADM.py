import colorama
from colorama import Fore


colorama.init(autoreset='true')
BOLD = '\033[1m'



def verUsuarios():

    """View de todos os usuarios"""
    print(f'Você está vendo todos os usuarios cadastrados ' + Fore.RESET)
    print(25 * '-')
    verUsuarios.view_users()