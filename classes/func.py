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

    def search(ong="", titulo="", id="", verify=""):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM campanha WHERE id=? or titulo=? or ong=?;", (id, titulo, ong,))
            rows = conecta.fetchall()
            if verify==False:
                print("{:<5} {:<20} {:<20} {:<40} {:<20} {:<20} ".format("ID", "ong", "titulo", "descricao","denuncia","meta"))
                
                for item in range(len(rows)): 
                    print("{:<5} {:<20} {:<20} {:<40} {:<20} {:<20} ".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3], rows[item][4], rows[item][5]))
            else:
                for item in rows:
                    if item != '':
                        conecta.disconnect()
                        return True
                    else:
                        conecta.disconnect()
                        return False
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Pesquisa realizada com sucesso.")
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

class Contato_Emerg:
    def view():
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("SELECT * FROM contatosEmerg;")
            
            rows = conecta.fetchall()
            print("{:<5} {:<20} {:<20}".format("ID", "autoridade", "Telefone"))
            
            for item in range(len(rows)):
                print("{:<5} {:<20} {:<20}".format(rows[item][0], rows[item][1], rows[item][2]))
        except Error as e: print(e)
        else: 
                input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def insert(autoridade, num):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("INSERT INTO contatosEmerg (autoridade, numTel) VALUES (?,?)", (autoridade, num,))
            conecta.persist()
        except Error as e: print(e)
        else:             
            print(Fore.GREEN + "Registro feito com sucesso.")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()

    def update(autoridade, num, id):
        conecta = Conexao()
        conecta.connect()
        try:
            conecta.execute("UPDATE contatosEmerg SET autoridade=?, numTel=? WHERE id = ?;",(autoridade, num, id))
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
            conecta.execute("DELETE FROM contatosEmerg WHERE id=?;", (id,))
            conecta.persist()
        except Error as e: print(e)
        else:
            print(Fore.GREEN + "Número de emergência removido com sucesso")
            input(Fore.BLUE + "Pressione <ENTER> para continuar...")
        finally: conecta.disconnect()