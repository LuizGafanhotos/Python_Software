from tkinter import *

app = Tk()
app.title("Titulo")
app.geometry("500x300")
app.configure(background="#dde")


#Anchor N => norte , S => sul, E =Leste , W = Oeste
#NE => noroeste, SE = sudeste, SO = sudoeste, NO= noroeste
Label(app,text="Nome",background="#dde", foreground="#009", anchor=W).place(x=10,y=10,width=100,height=20)


app.mainloop()