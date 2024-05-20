class Pessoa():

#Criando o metodo construtor e seus parametros
    def __init__ (self, nome):
        self.nome = nome
        self.comendo = False
        self.andando = False
        self.dormindo = False

#Criação dos metodos de ações e suas verificações
    def comer(self):

        if self.andando == False and self.dormindo == False:
            self.dormindo = True
            print(f"{self.nome} está comendo agora.")

#Metodos de parada para encerrar as ações
    def parar_comer(self):
        self.comendo = False
        print(f"{self.nome} terminou de comer, ele está de barriga cheia")

    def andar(self):

        if self.comendo == False and self.dormindo == False:
            self.andando = True
            print(f"{self.nome} está andando agora.")

    def parar_andar(self):
        self.andando = False
        print(f"{self.nome} parou de andar, ele está cansado.")

    def dormir(self):

        if self.comendo == False and self.andando == False:
            self.dormindo = True
            print(f"{self.nome} está dormindo agora.")

    def parar_dormir(self):
        self.dormindo = False
        print(f"{self.nome} acordou.")