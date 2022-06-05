from colorama import Fore
from .conexao import Conexao
from sqlite3 import Error

conecta = Conexao()
conecta.connect()

class Denuncia:
    def view():
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM denuncia;")
            
            rows = conecta.fetchall()
            print("{:<5} {:<40} {:<20} {:<15} {:<20} {:<20} ".format("ID", "nomeDenuncia", "telContato", "tipoDesastre","classificacao","situacao"))
            
            for item in range(len(rows)):
                print("{:<5} {:<40} {:<20} {:<15} {:<20} {:<20} ".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3], rows[item][4], rows[item][5]))
        except Error as e: print(e)
        else: 
                print(Fore.GREEN + "Pesquisa realizada com sucesso em Denuncias.")
                input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def insert(nomeDenuncia, telContato, tipoDesastre, classificacao, situacao=False):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("INSERT INTO denuncia (nomeDenuncia, telContato, tipoDesastre, classificacao, situacao) VALUES (?,?,?,?,?)", (nomeDenuncia, telContato, tipoDesastre, classificacao, situacao,))
            conecta.persist()
        except Error as e: print(e)
        else:             
            print(Fore.GREEN + "Registro feito com sucesso.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def update(nomeDenuncia, telContato, tipoDesastre, classificacao, situacao, id):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("UPDATE denuncia SET nomeDenuncia=?, telContato=?, tipoDesastre=?, classificacao=?, situacao=?: WHERE id = ?;",(nomeDenuncia, telContato, tipoDesastre, classificacao, situacao, id))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + 'Atualização feita com sucesso.')
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()   

    def search(id="", nomeDenuncia=""):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM denuncia WHERE id=? or nomeDenuncia=?;", (id, nomeDenuncia,))
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
            conecta.execute("DELETE FROM denuncia WHERE id=?;", (id,))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Rescadastro de Denuncia realizado com sucesso")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

class Campanha_Doacao:
    def view():
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM campanha;")
            
            rows = conecta.fetchall()
            print("{:<5} {:<20} {:<20} {:<40} {:<20} {:<20} ".format("ID", "ong", "titulo", "descricao","denuncia","meta"))
            
            for item in range(len(rows)):
                print("{:<5} {:<20} {:<20} {:<40} {:<20} {:<20} ".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3], rows[item][4], rows[item][5]))
        except Error as e: print(e)
        else: 
                print(Fore.GREEN + "Pesquisa realizada com sucesso em Campanhas.")
                input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def insert(ong, titulo, descricao, denuncia, meta):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("INSERT INTO campanha (ong, titulo, descricao, denuncia, meta) VALUES (?,?,?,?,?)", (ong, titulo, descricao, denuncia, meta,))
            conecta.persist()
        except Error as e: print(e)
        else:             
            print(Fore.GREEN + "Registro feito com sucesso.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def update(ong, titulo, descricao, denuncia, meta, id):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("UPDATE campanha SET ong=?, titulo=?, descricao=?, denuncia=?, meta=? WHERE id = ?;",(ong, titulo, descricao, denuncia, meta, id))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + 'Atualização feita com sucesso.')
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()       

    def delete(id):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("DELETE FROM campanha WHERE id=?;", (id,))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Descadastro de Campanhas realizado com sucesso")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()