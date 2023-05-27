print("Desafio 45")

from tkinter import *
from PIL import Image,ImageTk
from random import randint

#Minha Janela
root = Tk ()
root.title("Desafo 45")
root.configure(background="#ffffff")

#imagem
rock_img= ImageTk.PhotoImage(Image.open("pedra joken.png"))
paper_img= ImageTk.PhotoImage(Image.open("papel joken.png"))
tesoura_img= ImageTk.PhotoImage(Image.open("tesoura.png"))
rock_img_comp= ImageTk.PhotoImage(Image.open("pedra joken.png"))
paper_img_comp= ImageTk.PhotoImage(Image.open("papel joken.png"))
tesoura_img_comp= ImageTk.PhotoImage(Image.open("tesoura.png"))

#inserir imagem
user_label= Label(root,image=tesoura_img,bg="white")
comp_label= Label(root, image=tesoura_img_comp,bg="white")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)


#placar
playerScore= Label(root,text=0,font=100,bg="white", fg="#003366")
computerScore= Label(root,text=0,font=100,bg="white", fg="#003366")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#Indicador
user_indicator= Label(root, font=50, text= "Player",bg="white", fg="#003366")
computer_indicator= Label(root, font=50, text= "Computer",bg="white", fg="#003366")
user_indicator.grid(row=0,column=3)
computer_indicator.grid(row=0, column=1)

#mensagens
msg= Label(root, font=50,bg="white", fg="#003366")
msg.grid(row=3,column=2)

#Escolha de mensagem
def updateMessage(x):
    msg["text"] = x

#Placar do Jogador
def updateUserScore():
    score= int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

#Placar do computador
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

#verificação do ganhador
def checkwin(player,computer):
    if player == computer:
        updateMessage("É um empate!!!")
    elif player == "pedra":
        if computer == "papel":
            updateMessage("Você Perdeu")
            updateCompScore()
        else:
            updateMessage("Você Venceu")
            updateUserScore()
    elif player == "papel":
        if computer == "tesoura":
            updateMessage("Você Perdeu")
            updateCompScore()
        else:
            updateMessage("Você Venceu")
            updateUserScore()
    elif player == "tesoura":
        if computer == "pedra":
            updateMessage("Você Perdeu")
            updateCompScore()
        else:
            updateMessage("Você Venceu")
            updateUserScore()
    else:
        pass



#Escolha de Atualização

choices = ["pedra", "papel" , "tesoura"]
def updateChoice(x):

#Computador
    compChoice= choices[randint(0,2)]
    if compChoice == "pedra":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "papel":
        comp_label.configure(image=paper_img_comp)
    elif compChoice == "tesoura":
        comp_label.configure(image=tesoura_img_comp)

#Jogador
    if x=="pedra":
        user_label.configure(image=rock_img)
    elif x== "papel":
        user_label.configure(image=paper_img)
    elif x== "tesoura":
        user_label.configure(image=tesoura_img)

    checkwin(x,compChoice)




#botões
rock = Button(root, width=20,height=2,text="pedra",
            bg="#ff3e4d",fg="white",command= lambda: updateChoice("pedra")).grid(row=2,column=1)
paper = Button(root, width=20,height=2,text="papel",
            bg="#fad02e",fg="white",command= lambda: updateChoice("papel")).grid(row=2,column=2)
scissor = Button(root, width=20,height=2,text="tesoura",
            bg="#0abde3",fg="white",command= lambda: updateChoice("tesoura")).grid(row=2,column=3)



root.mainloop()