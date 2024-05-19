from Classes import *

#Chamada da função, adição de valores aos parametros e chamada de metodos

pou = Pessoa("Fred", 70, 22)

#Atribuindo a opção do usuario escolher a ação

escolha_inicio = input("Qual ação deseja fazer: Comer, Andar ou Dormir?")
escolha_parar = "a"

if escolha_inicio == "comer" or escolha_inicio == "Comer":
    pou.comer()

    #Opção do usuario parar a ação ou não
    escolha_parar = input("Deseja parar a ação?")
    
    if escolha_parar == "Sim" or escolha_parar == "sim" or escolha_parar == "S" or escolha_parar == "s":
        pou.parar()
    
    elif escolha_parar == "Não" or escolha_parar == "não" or escolha_parar == "n" or escolha_parar == "N":
        print("A ação ainda esta aconcetendo.")
    
    else:
        print("Escolha inexistente.")

elif escolha_inicio == "andar" or escolha_inicio == "Andar":
    pou.andar()
    escolha_parar = input("Deseja parar a ação?")
    
    if escolha_parar == "Sim" or escolha_parar == "sim" or escolha_parar == "S" or escolha_parar == "s":
        pou.parar()

    elif escolha_parar == "Não" or escolha_parar == "não" or escolha_parar == "n" or escolha_parar == "N":
        print("A ação ainda esta aconcetendo.")
    
    else:
        print("Escolha inexistente.")

elif escolha_inicio == "dormir" or escolha_inicio == "Dormir":
    pou.dormir()
    escolha_parar = input("Deseja parar a ação?")
    
    if escolha_parar == "Sim" or escolha_parar == "sim" or escolha_parar == "S" or escolha_parar == "s":
        pou.parar()

    elif escolha_parar == "Não" or escolha_parar == "não" or escolha_parar == "n" or escolha_parar == "N":
        print("A ação ainda esta aconcetendo.")
    
    else:
        print("Escolha inexistente.")

else:
    print("ação inexistente.")