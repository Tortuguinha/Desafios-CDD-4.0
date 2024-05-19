class Pessoa():

#Criando o metodo construtor e seus parametros
    def __init__ (self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.dormindo = False

#Criação dos metodos de ações e suas verificações
    def comer(self):

        if self.andando == True:

            self.comendo = False
            self.dormindo = False
            print(f"O {self.nome} não comer agora pois está andando.")
        
        elif self.dormindo == True:

            self.comendo = False
            self.andando = False
            print(f"O {self.nome} não pode comer agora pois está dormindo.")
        
        else:
            self.comendo = True
            self.andando = False
            self.dormindo = False
            print(f"O {self.nome} está comendo no momento.")
            
    def andar(self):

        if self.comendo == True:

            self.andando = False
            self.dormindo = False
            print(f"O {self.nome} não pode andar agora pois está comendo.")
        
        elif self.dormindo == True:

            self.comendo = False
            self.andando = False
            print(f"O {self.nome} não pode andar agora pois está dormindo.")
        
        else:

            self.andando = True
            self.comendo = False
            self.dormindo = False
            print(f"O {self.nome} está andando no momento.")

    def dormir(self):

        if self.comendo == True:

            self.andando = False
            self.dormindo = False
            print(f"O {self.nome} não pode dormir agora pois está comendo.")
        
        elif self.andando == True:

            self.comendo = False
            self.dormindo = False
            print(f"O {self.nome} não pode falar agora pois está dormindo.")

        else:
            
            self.dormindo = True
            self.comendo = False
            self.andando = False
            print(f"O {self.nome} está dormindo no momento")

#Adição de metodo de parada

    def parar(self):
        self.comendo = False
        self.andando = False
        self.dormindo = False
        print(f"O {self.nome} parou a ação.")