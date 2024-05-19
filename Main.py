from Classes import *

#Chamada da função, adição de valores aos parametros e chamada de metodos

pou = Pessoa("Fred", 70, 22)

#Atribuindo a opção do usuario escolher a ação

escolha_inicio = input("Qual ação deseja fazer: Comer, Andar ou Dormir?")

if escolha_inicio == "comer" or escolha_inicio == "Comer":
    pou.comer()

elif escolha_inicio == "andar" or escolha_inicio == "Andar":
    pou.andar()

elif escolha_inicio == "dormir" or escolha_inicio == "Dormir":
    pou.dormir()