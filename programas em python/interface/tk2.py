from tkinter import *


def impDados():
    print("Nome: %s" % vnome)
    print("Telelfone: %s" % vfone)

app = Tk()
app.title("Titulo")
app.geometry("500x300")
app.configure(background="#dde")


#Anchor N => norte , S => sul, E =Leste , W = Oeste
#NE => noroeste, SE = sudeste, SO = sudoeste, NO= noroeste
Label(app,text="Nome",background="#fff", foreground="#009", anchor=W).place(x=10,y=10,width=100,height=20)
vnome = Entry(app).place(x=10,y=30,width=200, height=20)

Label(app,text="Telefone",background="#fff", foreground="#009", anchor=W).place(x=10,y=60,width=100,height=20)
vfone = Entry(app).place(x=10,y=80,width=200, height=20)

Button(app,text="Imprimir",command=impDados).place(x=10,y=270,width=100,height=20)
app.mainloop()