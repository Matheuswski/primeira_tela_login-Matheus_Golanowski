#IMPORTAR AS BIBLIOTECAS
from tkinter import* #Importa todos os modulos do tkinter
from tkinter import messagebox #Importa o modulo de caixas de menssagem do tkinter
from tkinter import ttk #Importa o modulo de widgets tematicos do tkinter
from DataBase import Database #Importa a classe Database do modulo Database

#CRIAR A JANELA
jan = Tk() # Cria uma instancia da janela principal
jan.title("SL Sytens - Painel de Acesso") #Define o titulo da janela
jan.geometry("600x300") #Define o tamanho da janela
jan.configure(background="white") #Configura a cor de fundo da janela
jan.resizable(width=False,height=False) #Impede que a janela seja redirecionada

#COMANDO PARA DEIXAR A TELA TRANSPARENTE
jan.attributes("-alpha", 0.9) # Define a transparencia da janela (0.0 a 1.0)

#DEFINIR INCONE DA JANELA
#jan.iconbitmap(default="incons/LogosMatheusGolanowski.png") #Define o icone da janela

#CARREGAR IMAGEM
logo = PhotoImage(file="inconsLogoMatheusGolanowski.png") # Carrega a imagem do logo  

#CRIAR FRAME
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise") #Cria um frame á esquerda
LeftFrame.pack(side = LEFT) #Posiciona o frame a esquerda
RightFrame = Frame(jan,width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")#Cria um frame á direita
RightFrame.pack(side = RIGHT)#Posiciona o frame a direita

#ADICIONAR LOGO
LogoLabel = Label(LeftFrame,image=logo, bg="MIDNIGHTBLUE")#Cria um label para a imagem do logo
LogoLabel.place(x=50, y=100)#Posiciona o label no frame esquerdo

#ADICIONAR CAMPOS DE USUARIO E SENHA
UsuarioLabel = Label(RightFrame, text="Usuario: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")#Cria um label para o usuario
UsuarioLabel.place(x=5,y=100)#Posiciona o label no frame direito
UsuarioEntry = ttk.Entry(RightFrame,width=30)#Cria um campo de entrada para o usuario
UsuarioEntry.place(x=120, y=115)#Posiciona o campo de entrada
SenhaLabel = Label(RightFrame,text="Senha: ",font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")#Cria um label para senha
SenhaLabel.place(x=5,y=150)#Posiciona o campo de entrada
SenhaEntry = ttk.Entry(RightFrame, wifth=30,show=".")#cria um campo de entrada para a senha
SenhaEntry.place(x=120, y=165)#Posiciona o campo de entrada 

#FUNÇÃO DE LOGIN 
def Login():
    usuario = UsuarioEntry.get()#Obtem o valor do campo de entrada do usuario
    senha =SenhaEntry.get()#Obtem o valor do campo d entrada da senha

    # Conecta ao banco de dados
    db = Database()#Cria uma instancia da clase DataBase
    db.cursor.execute("""SELECT*FROM usuario WHERE usuario = %s AND senha = %s""",(usuario,senha))#Executa a consulta SQL para verificar o usuario e a senha
    VerifyLogin = db.cursor.fetchone() #Obtem o resultado da consulta 

    #Verifica se o usuario foi encontrado
    if VerifyLogin:
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado. Bem Vindo!")#Exibe menssagem de sucesso

    else:
        messagebox.showerror(title="INFO LOGIN",message="Acesso Negado. Verifique se está cadastrado no Sistema!")#Exibe menssagem erro

#CRIANDO BOTÕES
LoginButton = ttk.Button(RightFrame, text = "LOGIN", width=15, command=Login)#Cria um botão de login
LoginButton.place(x=150, y=225)#Posiciona o botão de login

#FUNÇÃO PARA REGISTRAR NOVO USUARIO
def Registrar():
    #REMOVER BOTÕES DE LOGIN
    LoginButton.place(x=5000)#Move o botão de loginpara fora da tela
    RegisterButton.place(x=5000)#Mover o botão de registro para fora da tela

    #INSERINDO WIDGETS DE CADASTRO
    NomeLabel = Label(RightFrame, text="Nome", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")#Cria um label para o nome
    NomeLabel.place(x=5, y=5)#posiciona o label no frame direito
    NomeEntry = ttk.Entry(RightFrame, width=30)#Cria um campo de entradapara o nome
    NomeEntry.place(x=120, y=20)#Posiciona o campo de entrada

    EmailLabel = Label(RightFrame, text="Email", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")#Cria um label para o email
    EmailLabel.place(x=5, y=40)#Posiciona o label no frame direito
    EmailEntry = ttk.Entry(RightFrame, width=30)#Cria um campo de entrada para o email
    EmailEntry.place(x=120, y=55)#Posiciona o campo de entrada

#FUNÇÃO PARA REGISTRAR NO BANCO DE DADOS
    def RegistrarNoBanco(): 
        nome = NomeEntry.get() #Obtém o valor do campo de entrada do nome
        email = EmailEntry.get() #Obtém o valor do campo de entrada do email
        usuario = UsuarioEntry.get() #Obtém o valor do campo de entrada do usuario
        senha = SenhaEntry.get() #Obtém o valor do campo de entrada da senha

    #Verifica se todos os campos estão preenchidos
        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de regidtro", message="PREENCHA TODOS OS CAMPOS") #Exibe mensagem de erro
        else:
            db = Database() #Cria uma instancia de classe Database
            db.RegistrarNoBanco(nome,email,usuario,senha) #Chama o método para registrar no banco de dados
            messagebox.showinfo("Sucesso", "Usuario registrado com sucesso!") #Exibe mensagem de sucesso

            #Limpar os campos após o registro
            NomeEntry.delete(0,END) #Limpa o campos de entrada do nome
            EmailEntry.delete(0,END) #Limpa o campos de entrada do email
            UsuarioEntry.delete(0,END) #Limpa o campos de entrada do usuario
            SenhaEntry.delete(0,END) #Limpa o campos de entrada da senha
Register = ttk.Button(RightFrame,text="REGISTRAR", width=15, command=RegistrarNoBanco) #Cria um botão de registro
Register.place(x=150, y=225) # Posiciona o botão de registro

#FUNÇÃO PARA VOLTAR Á TELA DE LOGIN
def VoltarLogin():
        NomeLabel.place(x=5000) #Move o label do nome para fora da tela
        NomeEntry.place(x=5000) #Move o campo de entrada do nome para fora da tela
        EmailLabel.place(x=5000) #Move o label do email para fora da tela
        EmailEntry.place(x=5000) #Move o campo de entrada do email para fora da tela
        Register.place(x=5000) #Move o botão de registro para fora da tela
        Voltar.place(x=5000) #Move o botão de voltar para fora da tela

    #TRAZENDO DE VOLTA OS WIDGETS
        LoginButton.place(x=150) #Traz o botão de login de volta para a tela
        RegisterButton.place(x=150) #Traz o botão de registro de voltapara a tela

Voltar = ttk.Button(RightFrame, text="VOLTAR", width=15, command=VoltarLogin) #Cria um botão de voltar
Voltar.palace(x=150, y=225) #Posiciona o botão de registro

#INICIAR O LOOP PRINCIPAL
jan.mainloop() # Inicia o loop principal da aplicação