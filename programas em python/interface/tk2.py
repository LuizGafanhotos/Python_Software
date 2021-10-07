from tkinter import *
import os
import tk3

c = os.path.dirname(__file__)
nomeArquivo = c+"\\nomes.txt"

def impDados():
    arquivo=open(nomeArquivo, "a")
    arquivo.write("\nNome:.....%s" % vnome.get())
    arquivo.write("\nTelelfone: %s" % vfone.get())
    arquivo.write("\n\n")
    arquivo.close()

app = Tk()
app.title("Titulo")
app.geometry("500x300")
app.configure(background="#dde")


#Anchor N => norte , S => sul, E =Leste , W = Oeste
#NE => noroeste, SE = sudeste, SO = sudoeste, NO= noroeste
Label(app,text="Nome",background="#fff", foreground="#009", anchor=W).place(x=10,y=10,width=100,height=20)
vnome = Entry(app)
vnome.place(x=10,y=30,width=200, height=20)

Label(app,text="Telefone",background="#fff", foreground="#009", anchor=W).place(x=10,y=60,width=100,height=20)
vfone = Entry(app)
vfone.place(x=10,y=80,width=200, height=20)

Label(app,text="E-mail",background="#fff", foreground="#009", anchor=W).place(x=10,y=70, width=100, height=20)
vemail = Entry(app)
vemail.place(x=10,y=180,width=300,height=80)

Label(app,text="OBS", background="#fff", foreground="#009", anchor=W).place(x=10, y=90, width=100,height=20)
vobs = Text(app)
vobs.place(x=10,y=180,width=300,height=80)

Button(app,text="Imprimir",command=impDados).place(x=10,y=270,width=100,height=20)
app.mainloop()