from distutils.spawn import find_executable
from colorama import Fore
from .conexao import Conexao
from sqlite3 import Error

conecta = Conexao()
conecta.connect()

class Usuario:
    def view():
        try:
            conecta.execute("SELECT * FROM usuario;")
            
            rows = conecta.fetchall()
            print("{:<5} {:<20} {:<50} {:<11}".format("ID", "Nome", "Email", "CPF"))
            
            for item in range(len(rows)):
                print("{:<5} {:<20} {:<50} {:<11}".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3]))
        
        except Error as e: print(e)
        else: 
            print(Fore.GREEN + "Pesquisa realizada com sucesso em Clientes.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def insert(nome, email, cpf):
        try:
            conecta.execute("INSERT INTO usuario (nome, email, cpf) VALUES (?,?,?)", (nome, email, cpf))
            conecta.persist()
        except Error as e: print(e)
        else:             
            print(Fore.GREEN + "Registro feito com sucesso.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def update(id, nome, email, cpf):
        try:
            conecta.execute("UPDATE usuario SET nome =?, email=?, cpf=? WHERE id = ?;",(nome, email, cpf, id))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + 'Atualização feita com sucesso.')
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def delete(id):
        try:
            conecta.execute("DELETE FROM usuario WHERE id=?;", (id,))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Descadastro de usuário realizado com sucesso")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()


class Ong:
    def __init__(self, nome, cnpj, endereco, email, telefone, bio):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.email = email  
        self.tel = telefone
        self.bio = bio
