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
            for item in range(len(rows)):
                print(Fore.GREEN +'ID: ' + Fore.RESET + f'{rows[item][0]}')
                print(Fore.GREEN +'Nome: ' + Fore.RESET + f'{rows[item][1]}')
                print(Fore.GREEN +'Email: ' + Fore.RESET + f'{rows[item][2]}')
                print(Fore.GREEN +'CPF: ' + Fore.RESET + f'{rows[item][3]}')
                print(Fore.YELLOW + 25 * '-')
        
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
            return True
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

    def search(cpf="", id=""):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM usuario WHERE cpf=? or id=?;", (cpf, id))
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
            for item in range(len(rows)):
                print(Fore.GREEN +'ID: ' + Fore.RESET + f'{rows[item][0]}')
                print(Fore.GREEN +'Nome: ' + Fore.RESET + f'{rows[item][1]}')
                print(Fore.GREEN +'CNPJ: ' + Fore.RESET + f'{rows[item][2]}')
                print(Fore.GREEN +'Endereço: ' + Fore.RESET + f'{rows[item][3]}')
                print(Fore.GREEN +'Email: ' + Fore.RESET + f'{rows[item][4]}')
                print(Fore.GREEN +'Telefone: ' + Fore.RESET + f'{rows[item][5]}')
                print(Fore.GREEN +'Descrição: ' + Fore.RESET + f'{rows[item][6]}')
                print(Fore.YELLOW + 25 * '-')
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

    def search(cnpj="", id=''):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM ong WHERE cnpj=? or id=?;", (cnpj, id))
            rows = conecta.fetchall()

            for item in range(len(rows)): 
                if item != '': 
                    conecta.disconnect()
                    return rows[item][0]
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

class Admin:
    def serch_campanha(idong):
            conecta = Conexao()
            conecta.connect()
            try:
                conecta.execute("SELECT * FROM campanha WHERE ong=?;", (idong,))
                rows = conecta.fetchall()

                for item in range(len(rows)): 
                    if item != '': 
                        conecta.disconnect()
                        return rows[item][0]
            except Error as e: print(e)
            finally: conecta.disconnect()

    def update_denuncia(sit,id):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("UPDATE denuncia SET situacao=? WHERE id = ?;",(sit,id))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + 'Atualização feita com sucesso.')
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect() 