from classes.conexao import Conexao

def initDB():
    conecta = Conexao()
    conecta.connect()
    #-----------Usuários do sistema-----------#
    conecta.execute(        
        "CREATE TABLE IF NOT EXISTS usuario (id integer primary key AUTOINCREMENT, nome TEXT NOT NULL, email TEXT NOT NULL, cpf TEXT NOT NULL);"
    )
    conecta.execute( 
        "CREATE TABLE IF NOT EXISTS ong (id integer primary key AUTOINCREMENT, nome TEXT NOT NULL, cnpj TEXT NOT NULL, endereco TEXT NOT NULL, email TEXT NOT NULL, tel TEXT NOT NULL, bio TEXT NOT NULL);"
    )
    #-----------Desastre, Local e Classificação-----------#
    conecta.execute(
        "CREATE TABLE IF NOT EXISTS tipoDesastre (id integer primary key AUTOINCREMENT, descricao TEXT NOT NULL);"
    )
    conecta.execute(
        "CREATE TABLE IF NOT EXISTS tipoLocal (id integer primary key AUTOINCREMENT, siglaEstado TEXT NOT NULL, cidade TEXT NOT NULL, logradouro TEXT NOT NULL, cep TEXT NOT NULL);"        
    )
    conecta.execute(     
        "CREATE TABLE IF NOT EXISTS classificacao (id integer primary key AUTOINCREMENT, descricao TEXT NOT NULL);"
    )
    #-----------Denúnica e Campanhas (Funcionalidades)-----------#
    conecta.execute( 
        "CREATE TABLE IF NOT EXISTS denuncia (id integer primary key AUTOINCREMENT, nomeDenunica TEXT NOT NULL, telContato TEXT NOT NULL, tipoDesastre TEXT NOT NULL, classificacao TEXT NOT NULL, situacao TEXT NOT NULL, foreign key(tipoDesastre) references tipoDesastre(id), foreign key(classificacao) references classificacao(id));"
    )
    conecta.execute( 
        "CREATE TABLE IF NOT EXISTS denuncia (id integer primary key AUTOINCREMENT, ong TEXT NOT NULL, titulo TEXT NOT NULL, descricao TEXT NOT NULL, denuncia TEXT NOT NULL, meta TEXT NOT NULL, foreign key(ong) references ong(id), foreign key(denuncia) references denuncia(id));"
    )
    conecta.persist()
    conecta.disconnect()
