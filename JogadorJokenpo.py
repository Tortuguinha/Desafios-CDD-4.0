class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def fazer_escolha(self, opcoes):
        while True:
            escolha = input(f"{self.nome}, escolha pedra, papel ou tesoura: ").lower()
            if escolha in opcoes:
                return escolha
            else:
                print("Escolha inválida. Tente novamente.")
