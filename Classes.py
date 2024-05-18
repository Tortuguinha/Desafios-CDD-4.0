class Pessoa():

#Criando o metodo construtor e seus parametros
    def __init__ (self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

#Criação dos metodos de ações e suas verificações
    def comer(self):

        if self.falando == True:

            self.comendo = False
            self.dormindo = False
            print(f"O {self.nome} não comer agora pois está falando.")
        
        elif self.dormindo == True:

            self.comendo = False
            self.falando = False
            print(f"O {self.nome} não pode comer agora pois está dormindo.")
        
        else:
            self.comendo = True
            self.falando = False
            self.dormindo = False
            print(f"O {self.nome} está comendo no momento.")

    def falar(self):

        if self.comendo == True:

            self.falando = False
            self.dormindo = False
            print(f"O {self.nome} não pode falar agora pois está comendo.")
        
        elif self.dormindo == True:

            self.comendo = False
            self.falando = False
            print(f"O {self.nome} não pode falar agora pois está dormindo.")
        
        else:

            self.falando = True
            self.comendo = False
            self.dormindo = False
            print(f"O {self.nome} está falando no momento.")

    def dormir(self):

        if self.comendo == True:

            self.falando = False
            self.dormindo = False
            print(f"O {self.nome} não pode dormir agora pois está comendo.")
        
        elif self.falando == True:

            self.comendo = False
            self.dormindo = False
            print(f"O {self.nome} não pode falar agora pois está dormindo.")

        else:
            
            self.dormindo = True
            self.comendo = False
            self.falando = False
            print(f"O {self.nome} está dormindo no momento")