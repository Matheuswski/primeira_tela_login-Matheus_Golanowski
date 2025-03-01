import mysql.connector #Importa o modulo mysql.connector para conectar ao banco de dados MySQL

class Database:
    def __init__(self):
        #Conecta ao banco de dados MySQL com as credencias fornecidads
        self.conn = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "",
            database = "MatheusGolanowski_db"
        )
        self.cursor = self.conn.cursor()#Cria um cursor para executar comandos SQL
        #Cria tabela "usuario1" se ela não existir
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS usuario1(
            idUsuario INT AUTO_INCREMENT PRIMARY KEY,
            nome TEXT(255),
            email TEXT(255),
            usuario TEXT(255),
            senha TEXT (255)
        );""")
        self.conn.commit() # Confirma a cria ção da tabela 

        print("conectado ao banco de dados") #Imprime uma mensagem de confirmação

#Metodo para registrar um noco usuario no banco de dadps
def RegistrarNoBanco(self, nome, email, usuario, senha):
    self.cursor.execute("INSERIR INTO usuario1 (nome,email, usuario, senha) VALUES (%s, %s, %s, %s)",
                        (nome,email, usuario, senha))#Inserir os dados do usuario na tabela 
    self.conn.commit()# Confirma a inserção dos dados 

    #Metodo para alterar os dados de um usuario existe no banco de dados
    def alterar(self, idUsuario, nome , email, usuario ,senha):
        self.cursor.execute("UPDATE usuario1 SET nome=%s, email=%s, usuario=%s, senha=%s WHERE idUsuario=%s",
                            (nome, email, usuario, senha, idUsuario))#Atualiza os dados do usuario com o id fornecido
        self.conn.commit() #Confirma a atualização dos dados

    #Metodo Para exluir um usuario do banco de dados 
    def excluir(self, idUsuario):
        self.cursor.execute("DELETE FROM usuario1 WHERE idUsuario %s",(idUsuario,))#Excluir o usuario com id fornecido
        self.conn.commit()# Confirma a exclusão dos dados 

    #Metodo para buscar os dados de um usuario no banco de dados
    def buscar(self,idUsuario):
        self.sursor.exucute("SELECT * FROM usuario1 WHERE idUsuario=%s",(idUsuario))#Retornar os dados do usuario encontrado 
        return self.cursor.fetchone()#Retornar os dados do usuario encontardo
    
    #MetodoChamado quando a instancia da classe é destruida
    def __del__(self):
        self.conn.close()#Fecha a conexão con o banco de dados 