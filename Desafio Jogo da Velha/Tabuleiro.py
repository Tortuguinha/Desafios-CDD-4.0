class Tabuleiro:
    def __init__(self):
        self.tabuleiro = {
            (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
            (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
            (2, 0): ' ', (2, 1): ' ', (2, 2): ' '
        }

    def imprimir_tabuleiro(self):
        for linha in range(3):
            for coluna in range(3):
                print(self.tabuleiro[(linha, coluna)], end='')
                if coluna < 2:
                    print('|', end='')
            print()
            if linha < 2:
                print('-' * 5)

    def marcar_posicao(self, linha, coluna, jogador):
        if self.tabuleiro[(linha, coluna)] == ' ':
            self.tabuleiro[(linha, coluna)] = jogador
            return True
        else:
            print("Posição já ocupada. Tente novamente.")
            return False

    def verificar_vitoria(self):
        # Verificar linhas
        for linha in range(3):
            if (self.tabuleiro[(linha, 0)] == self.tabuleiro[(linha, 1)] ==
                    self.tabuleiro[(linha, 2)]) and self.tabuleiro[(linha, 0)] != ' ':
                return True

        # Verificar colunas
        for coluna in range(3):
            if (self.tabuleiro[(0, coluna)] == self.tabuleiro[(1, coluna)] ==
                    self.tabuleiro[(2, coluna)]) and self.tabuleiro[(0, coluna)] != ' ':
                return True

        # Verificar diagonais
        if (self.tabuleiro[(0, 0)] == self.tabuleiro[(1, 1)] == self.tabuleiro[(2, 2)] or
                self.tabuleiro[(0, 2)] == self.tabuleiro[(1, 1)] == self.tabuleiro[(2, 0)]) and self.tabuleiro[(1, 1)] != ' ':
            return True

        return False

    def tabuleiro_cheio(self):
        for coordenada in self.tabuleiro.values():
            if coordenada == ' ':
                return False
        return True
