from tkinter import *

janelito = Tk()

lb = Label(janelito, text="Ola mundo lindo e maravilhoso")
lb.place(x=300, y=330)

janelito.geometry("200x200+300+300")
janelito.mainloop()