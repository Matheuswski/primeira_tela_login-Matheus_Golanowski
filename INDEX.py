#IMPORTAR AS BIBLIOTECAS
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

#CRIAR A JANELA
jan = Tk()
jan.title("SL Sytens - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False,height=False)

#COMANDO PARA DEIXAR A TELA TRANSPARENTE
jan.attributes("-alpha", 0.9)
#DEFINIR INCONE DA JANELA
jan.iconbitmap(default="incons/LogosMatheusGolanowski.png")
#CARREGAR IMAGEM
logo = PhotoImage(file="inconsLogoMatheusGolanowski.png")
#CRIAR FRAME
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side = LEFT)
RightFrame = Frame(jan,width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side = RIGHT)
#ADICIONAR LOGO
LogoLabel = Label(LeftFrame,image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)
#ADICIONAR CAMPOS DE USUARIO E SENHA
UsuarioLabel = Label(RightFrame, text="Usuario: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
UsuarioLabel.place(x=5,y=100)
UsuarioEntry = ttk.Entry(RightFrame,width=30)
UsuarioEntry.palce(x=120, y=115)
SenhaLabel = Label(RightFrame,text="Senha: ",font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
SenhaLabel.paklce(x=5,y=150)
SenhaEntry = ttk.Entry(RightFrame, wifth=30,show=".")
SenhaEntry.palce(x=120, y=165)

#FUNÇÃO DE LOGIN 
def Login():
    usuario = UsuarioEntry.get()
    senha =SenhaEntry.get()

    db = Database()
    db.cursor.execute("""
    SELECT*FROM usuario
    WHERE usuario = %s aAND senha = %s""",(usuario,senha))
    VerifyLogin = db.cursor.fetchone()

    if VerifyLogin:
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado. Bem Vindo!")

    else:
        messagebox.showerror(title="INFO LOGIN",message="Acesso Negado. Verifique se está cadastrado no Sistema!")

#CRIANDO BOTÕES
LoginButton = ttk.Button(RightFrame, text = "LOGIN", width=15, command=Login)
LoginButton.place(x=150, y=225)

#FUNÇÃO PARA REGISTRAR NOVO USUARIO
def Registrar():
    #REMOVER BOTÕES DE LOGIN