from pycep_correios import get_address_from_cep, WebService

def buscaCEP(cep):
    address = get_address_from_cep(f'{cep}', webservice=WebService.VIACEP)

    for key, value in address.items():
        if key == 'uf': sigla = value
        if key == 'cidade': cidade = value
        if key == 'logradouro': logradouro = value
    
    return sigla, cidade, logradouro