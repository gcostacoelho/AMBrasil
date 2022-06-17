import re

def valid(info, type):
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
