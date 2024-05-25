from JogadorJokenpo import Jogador

class JogoPedraPapelTesoura:
    def __init__(self):
        self.jogador1 = Jogador("Jogador 1")
        self.jogador2 = Jogador("Jogador 2")
        self.opcoes = ['pedra', 'papel', 'tesoura']
        self.resultado = {'pedra': {'tesoura': 'Que pena, pedra quebra tesoura!', 'papel': 'Parabéns, papel cobre pedra!'},
                          'papel': {'pedra': 'Que pena, papel cobre pedra!', 'tesoura': 'Parabéns, tesoura corta papel!'},
                          'tesoura': {'pedra': 'Parabéns, pedra quebra tesoura!', 'papel': 'Que pena, tesoura corta papel!'}}

    def jogar(self):
        escolha_jogador1 = self.jogador1.fazer_escolha(self.opcoes)
        escolha_jogador2 = self.jogador2.fazer_escolha(self.opcoes)

        print(f"{self.jogador1.nome} escolheu: {escolha_jogador1}")
        print(f"{self.jogador2.nome} escolheu: {escolha_jogador2}")

        if escolha_jogador1 == escolha_jogador2:
            print("Empate!")
        elif self.resultado[escolha_jogador1][escolha_jogador2]:
            print(self.resultado[escolha_jogador1][escolha_jogador2])
        else:
            print(self.resultado[escolha_jogador2][escolha_jogador1])

