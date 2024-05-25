from Tabuleiro import Tabuleiro
from JogadorVelha import Jogador

jogador1 = Jogador("Jogador 1", 'X')
jogador2 = Jogador("Jogador 2", 'O')
tabuleiro = Tabuleiro()
jogador_atual = jogador1

while not tabuleiro.tabuleiro_cheio():
    tabuleiro.imprimir_tabuleiro()
    jogador_atual.jogar(tabuleiro)

    if tabuleiro.verificar_vitoria():
        print(f"Parabéns, {jogador_atual.nome} venceu!")
        break

    if jogador_atual == jogador1:
        jogador_atual = jogador2
    else:
        jogador_atual = jogador1

else:
    print("Empate!")