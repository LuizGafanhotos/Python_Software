import tkinter

panel = tkinter.Tk()
panel.title("Primeira janela")
panel["bg"] = "blue"

#Largura x Altura + Esquerda + topo
panel.geometry("800x440+100+100")
panel.mainloop()