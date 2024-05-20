from Classes import *

#Chamada da função, adição de valores aos parametros e chamada de metodos

pou = Pessoa("Fred")

#Atribuindo a opção do usuario escolher a ação

escolha_inicio = int(input("Qual ação deseja fazer? \n 1 para Come \n 2 para andar \n 3 para dormir?"))
escolha_parar = 0

if escolha_inicio == 1:
    pou.comer()

    #Opção do usuario parar a ação ou não
    escolha_parar = int(input("Deseja parar a ação? \n 1 para sim \n 2 para não."))
    
    if escolha_parar == 1:
        pou.parar_comer()
    
    elif escolha_parar == 2:
        print(f"{pou.nome} ainda está comendo. Saco vazio não para em pé!")

        while escolha_parar == 2:
            escolha_parar = int(input("Deseja parar a ação? \n 1 para sim \n 2 para não."))
            
            if escolha_parar == 1:
                pou.parar_comer()
    
    elif escolha_parar != 0:
        print("Escolha inexistente.")

elif escolha_inicio == 2:
    pou.andar()

    escolha_parar = int(input("Deseja parar a ação? \n 1 para sim \n 2 para não."))
    
    if escolha_parar == 1:
        pou.parar_andar()
    
    elif escolha_parar == 2:
        print(f"{pou.nome} ainda está andando. Bora chegar na africa a pé!")

        while escolha_parar == 2:
            escolha_parar = int(input("Deseja parar a ação? \n 1 para sim \n 2 para não."))

            if escolha_parar == 1:
                pou.parar_andar()

    elif escolha_parar != 0:
        print("Escolha inexistente.")

elif escolha_inicio == 3:
    pou.dormir()
    
    escolha_parar = int(input("Deseja parar a ação? \n 1 para sim \n 2 para não."))
    
    if escolha_parar == 1:
        pou.parar_dormir()
    
    elif escolha_parar == 2:
        print(f"{pou.nome} ainda está dormindo. Belo adormecido!")

        while escolha_parar == 2:
            escolha_parar = int(input("Deseja parar a ação? \n 1 para sim \n 2 para não."))
    
            if escolha_parar == 1:
                pou.parar_dormir()

    elif escolha_parar != 0:
        print("Escolha inexistente.")

else:
    print("Ação inexistente.")