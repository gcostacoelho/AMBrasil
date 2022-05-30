from colorama import Fore
from .conexao import Conexao
from sqlite3 import Error

conecta = Conexao()
conecta.connect()

class Tipo_Desastre:
    def view():
        try:
            conecta.execute("SELECT * FROM tipoDesastre;")
            
            rows = conecta.fetchall()
            print("{:<5} {:<55} ".format("ID", "descricao",))
            
            for item in range(len(rows)):
                print("{:<5} {:<20}".format(rows[item][0], rows[item][1]))
        
        except Error as e: print(e)
        else: 
            print(Fore.GREEN + "Pesquisa realizada com sucesso em Clientes.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def insert(descricao):
        try:
            conecta.execute("INSERT INTO tipoDesastre (descricao) VALUES (?)", (descricao))
            conecta.persist()
        except Error as e: print(e)
        else:             
            print(Fore.GREEN + "Registro feito com sucesso.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def update(id, descricao):
        try:
            conecta.execute("UPDATE tipoDesastre SET descricao=? WHERE id = ?;",(descricao, id))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + 'Atualização feita com sucesso.')
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def delete(id):
        try:
            conecta.execute("DELETE FROM tipoDesastre WHERE id=?;", (id,))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Descadastro de usuário realizado com sucesso")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()


class Tipo_Local:
    def view():
        try:
            conecta.execute("SELECT * FROM tipoLocal;")
            
            rows = conecta.fetchall()
            print("{:<5} {:<20} {:<50} {:<11} {:<20} ".format("ID", "SiglaEstado", "Cidade", "Logradouro","CEP",))
            
            for item in range(len(rows)):
                print("{:<5} {:<20} {:<50} {:<11} {:<20} ".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3], rows[item][4]))
        except Error as e: print(e)
        else: 
                print(Fore.GREEN + "Pesquisa realizada com sucesso em Clientes.")
                input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def insert(siglaEstado, cidade, logradouro, cep):
        try:
            conecta.execute("INSERT INTO tipoLocal (siglaEstado, cidade, logradouro, cep) VALUES (?,?,?,?)", (siglaEstado, cidade, logradouro, cep,))
            conecta.persist()
        except Error as e: print(e)
        else:             
            print(Fore.GREEN + "Registro feito com sucesso.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def update(siglaEstado, cidade, logradouro, cep, id):
        try:
            conecta.execute("UPDATE tipoLocal SET siglaEstado=?, cidade=?, logradouro=?, cep=?: WHERE id = ?;",(siglaEstado, cidade, logradouro, cep, id))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + 'Atualização feita com sucesso.')
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def delete(id):
        try:
            conecta.execute("DELETE FROM tipoLocal WHERE id=?;", (id,))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Descadastro de usuário realizado com sucesso")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()


class Classificacao:
    def view():
        try:
            conecta.execute("SELECT * classificacao ;")
            
            rows = conecta.fetchall()
            print("{:<5} {:<55} ".format("ID", "descricao",))
            
            for item in range(len(rows)):
                print("{:<5} {:<20}".format(rows[item][0], rows[item][1]))
        
        except Error as e: print(e)
        else: 
            print(Fore.GREEN + "Pesquisa realizada com sucesso em Clientes.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def insert(descricao):
        try:
            conecta.execute("INSERT INTO classificacao (descricao) VALUES (?)", (descricao))
            conecta.persist()
        except Error as e: print(e)
        else:             
            print(Fore.GREEN + "Registro feito com sucesso.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def update(id, descricao):
        try:
            conecta.execute("UPDATE classificacao SET descricao=? WHERE id = ?;",(descricao, id))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + 'Atualização feita com sucesso.')
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def delete(id):
        try:
            conecta.execute("DELETE FROM classificacao WHERE id=?;", (id,))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Descadastro de usuário realizado com sucesso")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()
