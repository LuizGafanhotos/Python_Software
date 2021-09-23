from tkinter import *

app = Tk()
app.title("Interface Desktop")
app.geometry("500x300")
app.configure(background="#008")

txtl = Label(app, text="Ola mundo", background="#ff0",foreground="#000")
txtl.place(x=10,y=10,width=160,height=30)

vtxt="Modulo TKINTER"
vbg = "#008"
vfg = "#fff"
txt2 = Label(app, text=vtxt,background=vbg,foreground=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=X,expand=True) #left right bottom top
app.mainloop()