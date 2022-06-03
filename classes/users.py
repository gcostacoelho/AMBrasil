from colorama import Fore
from .conexao import Conexao
from sqlite3 import Error

conecta = Conexao()
conecta.connect()

class Usuario:
    def view():
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM usuario;")
            
            rows = conecta.fetchall()
            print("{:<5} {:<20} {:<50} {:<11}".format("ID", "Nome", "Email", "CPF"))
            
            for item in range(len(rows)):
                print("{:<5} {:<20} {:<50} {:<11}".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3]))
        
        except Error as e: print(e)
        else: 
            print(Fore.GREEN + "Pesquisa realizada com sucesso em Usuário.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def insert(nome, email, cpf):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("INSERT INTO usuario (nome, email, cpf) VALUES (?,?,?)", (nome, email, cpf))
            conecta.persist()
        except Error as e: print(e)
        else:             
            print(Fore.GREEN + "Registro feito com sucesso.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def update(id, nome, email, cpf):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("UPDATE usuario SET nome =?, email=?, cpf=? WHERE id = ?;",(nome, email, cpf, id))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + 'Atualização feita com sucesso.')
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def search(cpf=""):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM usuario WHERE cpf=?;", (cpf,))
            rows = conecta.fetchall()

            for item in rows: 
                if item != '': 
                    conecta.disconnect()
                    return True
        except Error as e: print(e)
        finally: conecta.disconnect()

    def delete(id):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("DELETE FROM usuario WHERE id=?;", (id,))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Descadastro de usuário realizado com sucesso")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

class Ong:
    def view():
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM ong;")
            
            rows = conecta.fetchall()
            print("{:<5} {:<20} {:<50} {:<11} {:<40} {:<30} {:22}".format("ID", "Nome", "Cnpj", "Endereço","Email","telefone","biografia"))
            
            for item in range(len(rows)):
                print("{:<5} {:<20} {:<50} {:<11} {:<40} {:<30} {:22}".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3], rows[item][4], rows[item][5], rows[item][6]))
        except Error as e: print(e)
        else: 
                print(Fore.GREEN + "Pesquisa realizada com sucesso em Ong.")
                input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def insert(nome, cnpj, endereco, email, tel, bio):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("INSERT INTO ong (nome, email, cnpj, endereco, tel, bio) VALUES (?,?,?,?,?,?)", (nome, cnpj, endereco, email, tel, bio,))
            conecta.persist()
        except Error as e: print(e)
        else:             
            print(Fore.GREEN + "Registro feito com sucesso.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def update(nome, cnpj, endereco, email, tel, bio, id):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("UPDATE ong SET nome =?, cnpj=?, endereco=? , email=?, tel=?, bio=? WHERE id = ?;",(nome, cnpj, endereco, email, tel, bio, id))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + 'Atualização feita com sucesso.')
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def search(cnpj=""):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM ong WHERE cnpj=?;", (cnpj,))
            rows = conecta.fetchall()

            for item in rows: 
                if item != '': 
                    conecta.disconnect()
                    return True
        except Error as e: print(e)
        finally: conecta.disconnect()
        
    def delete(id):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("DELETE FROM ong WHERE id=?;", (id,))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Descadastro de usuário realizado com sucesso")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()
