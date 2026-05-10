# Declaração da Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instãncia
        self.nome = ""
        self.idade = 0
        
    # Métodos de Intância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome.capitalize()} é um(a) Gafanhoto(a) e tem {self.idade} anos."

# Declaração do Objeto
gafanhoto001 = Gafanhoto()
gafanhoto001.nome = "maria"
gafanhoto001.idade = 17
gafanhoto001.aniversario()
print(gafanhoto001.mensagem())

gafanhoto002 = Gafanhoto()
gafanhoto002.nome = "mauro"
gafanhoto002.idade = 53
gafanhoto002.aniversario()
print(gafanhoto002.mensagem())

gafanhoto003 = Gafanhoto()
print(gafanhoto003.mensagem())