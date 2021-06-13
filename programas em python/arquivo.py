class NPC:
    def __init__(self,nome,time,forca,municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
    
    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Time: {self.time}")
        print(f"forca: {self.forca}")
        print(f"municao: {self.municao}")
        print("vivo: " + ("sim" if self.vivo else "não"))
        print(f"Energia {str(self.energia)}")
        print("-"*30)

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 300
        super().__init__(nome,time,self.forca,self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 500
        self.municao = 41
        super().__init__(nome, time, self.forca, self.municao)

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 600
        self.municao = 78
        super().__init__(nome, time, self.forca, self.municao)

class Lider(NPC):
    def __init__(self, nome, time):
        self.forca = 10000000000
        self.municao = 100000000
        super().__init__(nome, time, self.forca, self.municao)
    def information(self):
        super().info
        
soldier1=Guarda("Olho vivo",1)
soldier2=Soldado("Bala na quenga",2)
soldier3=Elite("Paulotejando",1)
soldier4=Guarda("Jogador de free fire",1)
soldier5=Lider("Adolfer josepher",1)

soldier1.info()
soldier2.info()
soldier3.info()
soldier4.info()
soldier5.info()