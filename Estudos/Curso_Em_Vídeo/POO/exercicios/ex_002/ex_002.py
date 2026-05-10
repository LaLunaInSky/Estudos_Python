# Declaração da Classe
class Gafanhoto:
    """
    Esta classe cria um gafanhoto que possue nome e idade, podendo fazer aniversário e também se apresentar.

    * Para instânciar é preciso informar um nome que é um string e uma idade que é um inteiro, exemplo:

        variavel_do_objeto = Gafanhoto("Julio", 19)
    """
    def __init__(
        self,
        nome = "", 
        idade = 0
    ): # Método Construtor
        # Atributos de Instãncia
        self.nome = nome
        self.idade = idade
        
    # Métodos de Intância
    def aniversario(self):
        """
        O Método do aniversário irá acrescentar 1 a idade do gafanhoto, exemplo:
        
            variavel_do_objeto.aniversário()
        
        Neste exemplo o gafanhoto de 19 anos, ficará com 20 anos.
        """
        self.idade += 1

    def mensagem(self):
        """
        O Método de apresentação irá retornar uma string com o seguinte texto:
        
            "{nome_do_objeto} é um(a) Gafanhoto(a) e tem {idade_do_objeto} anos."
        
        Para a sua utilização, basta seguir o modelo:
        
            variavel_do_objeto.mensagem()
        """
        return f"{self.nome.capitalize()} é um(a) Gafanhoto(a) e tem {self.idade} anos."

    def __str__(self):
        return f"{self.nome.capitalize()} é um(a) Gafanhoto(a) e tem {self.idade} anos."

    def __getstate__(self):
        return f"\nState of Object:\nnome = {self.nome}, idade = {self.idade}\n"

# Declaração do Objeto
print(Gafanhoto.__doc__) # Dunder Attribute

# Instanciamento do gafanhoto001
gafanhoto001 = Gafanhoto(
    "maria", 17
)

gafanhoto001.aniversario()
print(gafanhoto001) # Dunder Method

print(gafanhoto001.__dict__) # Attribute
print(gafanhoto001.__getstate__()) # Method

# Instanciamento do gafanhoto002
gafanhoto002 = Gafanhoto(
    "mauro", 53
)

gafanhoto002.aniversario()
print(gafanhoto002)

print(gafanhoto002.__getstate__())
print(gafanhoto002.__class__)

# Instanciamento do gafanhoto003
gafanhoto003 = Gafanhoto()

print(gafanhoto003)