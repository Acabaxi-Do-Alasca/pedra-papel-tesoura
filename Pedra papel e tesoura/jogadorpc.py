import random
from jogador import Jogador

class JogadorComputador(Jogador):
    def obter_escolha(self):
        self.escolha = random.choice(["pedra", "papel", "tesoura"])