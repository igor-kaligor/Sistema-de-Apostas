class Jogador:
    def __init__(self, nome, jogo):
        self.nome = nome
        self.jogo = jogo
    def set_Nome(self,nome):
        self.nome = nome
    def get_Nome(self):
        return self.nome
    def set_Jogo(self,jogo):
        self.jogo = jogo
    def get_Jogo(self):
        return self.jogo
    def __str__():
        return "nome: " + nome + " , " + "jogo: " + jogo
