from jogador import Jogador

class JogadorHumano(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
        
    def obter_escolha(self):
        while True:
            escolha = input(f"{self.nome}, escolha pedra, papel ou tesoura: ")
            if escolha.lower() in ["pedra", "papel", "tesoura"]:
                self.escolha = escolha.lower()
                break
            else:
                print("Escolha inválida! Tente novamente.")