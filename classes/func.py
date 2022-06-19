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
            conecta.execute("SELECT d.id, d.nomeDenuncia, d.telContato, td.descricao, c.descricao, d.situacao from denuncia d inner join tipoDesastre td on td.id = d.tipoDesastre inner join classificacao c on c.id = d.classificacao;")
            rows = conecta.fetchall()
            for item in range(len(rows)):
                print(Fore.GREEN +'ID: ' + Fore.RESET + f'{rows[item][0]}')
                print(Fore.GREEN +'Denúncia: ' + Fore.RESET + f'{rows[item][1]}')
                print(Fore.GREEN +'Telefone: ' + Fore.RESET + f'{rows[item][2]}')
                print(Fore.GREEN +'Tipo de desastre: ' + Fore.RESET + f'{rows[item][3]}')
                print(Fore.GREEN +'Classificação: ' + Fore.RESET + f'{rows[item][4]}')
                print(Fore.GREEN +'Situação: ' + Fore.RESET + f'{rows[item][5]}')
                print(Fore.YELLOW + 25 * '-')
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
            conecta.execute("SELECT c.id, o.nome, c.titulo, c.descricao, d.nomeDenuncia, c.meta from campanha c inner join ong o on o.id = c.ong inner join denuncia d on d.id = c.denuncia; ")
            
            rows = conecta.fetchall()
            for item in range(len(rows)):
                print(Fore.GREEN +'ID: ' + Fore.RESET + f'{rows[item][0]}')
                print(Fore.GREEN +'Ong: ' + Fore.RESET + f'{rows[item][1]}')
                print(Fore.GREEN +'Titulo: ' + Fore.RESET + f'{rows[item][2]}')
                print(Fore.GREEN +'Descrição ' + Fore.RESET + f'{rows[item][3]}')
                print(Fore.GREEN +'Denúnica: ' + Fore.RESET + f'{rows[item][4]}')
                print(Fore.GREEN +'Meta: ' + Fore.RESET + f'{rows[item][5]}')
                print(Fore.YELLOW + 25 * '-')

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

    def search(idCampanha='', titulo='', ong='', verify=False):
        conecta = Conexao()
        conecta.connect()
        try:
            if verify==False:
                conecta.execute("SELECT c.id, o.nome, c.titulo, c.descricao, d.nomeDenuncia, c.meta from campanha c inner join ong o on o.id = c.ong inner join denuncia d on d.id = c.denuncia WHERE c.id=? or c.titulo=? or o.id=?;", (idCampanha, titulo, ong,))
                rows = conecta.fetchall()
                for item in range(len(rows)):
                    print(Fore.GREEN +'ID: ' + Fore.RESET + f'{rows[item][0]}')
                    print(Fore.GREEN +'Ong: ' + Fore.RESET + f'{rows[item][1]}')
                    print(Fore.GREEN +'Titulo: ' + Fore.RESET + f'{rows[item][2]}')
                    print(Fore.GREEN +'Descrição ' + Fore.RESET + f'{rows[item][3]}')
                    print(Fore.GREEN +'Denúnica: ' + Fore.RESET + f'{rows[item][4]}')
                    print(Fore.GREEN +'Meta: ' + Fore.RESET + f'{rows[item][5]}')
                    print(Fore.YELLOW + 25 * '-')
            else:
                conecta.execute("SELECT * FROM campanha WHERE id=? and ong=?;", (idCampanha, ong,))
                rows = conecta.fetchall()
                
                for item in range(len(rows)): 
                    if item != '':
                        conecta.disconnect()
                        return rows[item][0]
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