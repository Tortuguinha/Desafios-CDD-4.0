class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo

    def jogar(self, tabuleiro):
        while True:
            try:
                linha = int(input(f"{self.nome}, escolha uma linha (0, 1, 2): "))
                coluna = int(input(f"{self.nome}, escolha uma coluna (0, 1, 2): "))
                if 0 <= linha <= 2 and 0 <= coluna <= 2:
                    if tabuleiro.marcar_posicao(linha, coluna, self.simbolo):
                        break
            except ValueError:
                print("Entrada inválida. Tente novamente.")
