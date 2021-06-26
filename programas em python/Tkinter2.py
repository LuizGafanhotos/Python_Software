from tkinter import * 

window = Tk()

lb = Label(window, text="Ola mundo")
lb.place(x=70,y=70)

window.geometry("200x200+300+300")
window.mainloop()