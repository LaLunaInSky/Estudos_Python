from random import randint

class ContaBacaria:
    """
    Classe para criar um conta bancária, com a possibilidade de saques e depósitos

    Basta instânciar desta forma:
        nome_do_objeto = ContaBancaria(nome_do_titular: str)
    """
    def __init__(
        self, 
        nome_do_titular
    ) -> None:
        self.numero_da_conta = randint(1, 5000)
        self.titular = nome_do_titular
        self.saldo = 0.0

        print(f"\nOlá {self.titular.title()} sua conta de número {self.numero_da_conta} foi criada com sucesso.")

    def __str__(self) -> str:
        return f"\nA conta de número '{self.numero_da_conta}' do titular '{self.titular.title()}' possui o saldo de R${self.saldo:,.2f}."
    
    def sacar(
        self,
        valor_do_saque = 2.0
    ) -> None:
        if valor_do_saque <= self.saldo:
            self.saldo -= valor_do_saque

            print(f"\n{self.titular.title()} o saque de R${valor_do_saque:,.2f} foi realizado com sucesso.")
        else:
            print(f"\n{self.titular.title()} não possui saldo suficiente para o saque no valor de R${valor_do_saque:,.2f}.")

    def depositar(
        self,
        valor_do_deposito = 1.0
    ) -> None:
        self.saldo += valor_do_deposito

        print(f"\n{self.titular.title()} o depósito de R${valor_do_deposito:,.2f} foi realizado com sucesso.")

conta_luiz = ContaBacaria("luiz de melo")
print(conta_luiz)

conta_luiz.depositar(3000)
print(conta_luiz)

conta_luiz.depositar(500)
print(conta_luiz)

conta_luiz.sacar(3499)
print(conta_luiz)

conta_luiz.sacar()
print(conta_luiz)