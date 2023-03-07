class Jogo:
    def __init__(self):
        self.jogadores = []
        self.jogador_atual = None
        self.resultado = None
        self.sair = False

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def jogar(self):
        while not self.sair:
            for jogador in self.jogadores:
                self.jogador_atual = jogador
                jogador.obter_escolha()

            self.avaliar_resultado()
            self.mostrar_resultado()

            opcao = input("Deseja jogar novamente? (s/n): ")
            if opcao.lower() == "n":
                self.sair = True

    def avaliar_resultado(self):
        jogada1 = self.jogadores[0].escolha
        jogada2 = self.jogadores[1].escolha

        if jogada1 == jogada2:
            self.resultado = "Empate"
        elif jogada1 == "pedra" and jogada2 == "tesoura":
            self.resultado = f"{self.jogadores[0].nome} venceu!"
        elif jogada1 == "papel" and jogada2 == "pedra":
            self.resultado = f"{self.jogadores[0].nome} venceu!"
        elif jogada1 == "tesoura" and jogada2 == "papel":
            self.resultado = f"{self.jogadores[0].nome} venceu!"
        else:
            self.resultado = f"{self.jogadores[1].nome} venceu!"

    def mostrar_resultado(self):
        print(f"{self.jogadores[0].nome}: {self.jogadores[0].escolha}")
        print(f"{self.jogadores[1].nome}: {self.jogadores[1].escolha}")
        print(self.resultado)
        print()