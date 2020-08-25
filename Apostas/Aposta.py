class Aposta:
    def __init__(self, Nome, CPF, Email, Telefone, Quantidade, Jogo, Jogador):
        self.Nome = Nome
        self.CPF = CPF
        self.Email = Email
        self.Telefone = Telefone
        self.Quantidade = Quantidade
        self.Jogo = Jogo
        self.Jogador = Jogador

    def get_Nome(self):
        return self.Nome

    def get_CPF(self):
        return self.CPF

    def get_Email(self):
        return self.Email

    def get_Telefone(self):
        return self.Telefone

    def get_Quantidade(self):
        return self.Quantidade

    def get_Jogo(self):
        return self.Jogo

    def get_Jogador(self):
        return self.Jogador


    def __str__():
        return "Nome: " + Nome + " , " + "CPF: " + CPF + " , " + "Email: " + Email + " , " + "Telefone: " + Telefone + " , " + "Quantidade: " + Quantidade + " , " + "Jogo: " + Jogo + " , " + "Jogador: " + Jogador
