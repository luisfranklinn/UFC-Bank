class Conta:
    def __init__(self, cliente, num_conta, saldo, tipo_conta, senha_conta):
        self.cliente = cliente
        self.num_conta = num_conta
        self.saldo = saldo
        self.tipo_conta = tipo_conta
        self.senha_conta = senha_conta

    def saque(self, valor):
        if valor == 0:
            print(f"\nNão foi possível realizar a operação. Valor inválido.")
        elif valor > self.saldo:
            print("\nNão foi possível realizar a operação. Valor maior que o disponível em saldo.")
        else:
            self.saldo -= valor
            print(f"\n-R${valor} | Novo saldo: R${self.saldo}")


    def saque_transf(self, valor):
        if valor == 0:
            print(f"\nNão foi possível realizar a operação. Valor inválido.")
        elif valor > self.saldo:
            print("\nNão foi possível realizar a operação. Valor maior que o disponível em saldo.")
        else:
            self.saldo -= valor


    def deposito(self, valor):
        if valor < 0 and valor == 0:
            print(f"\nNão foi possível realizar a operação. Valor inválido ou insuficiente.")
        else:
            self.saldo += valor
            print(f"\n+R${valor} | Novo saldo: R${self.saldo}")


    def deposito_transf(self, valor):
        if valor < 0 and valor == 0:
            print(f"\nNão foi possível realizar a operação. Valor inválido ou insuficiente.")
        else:
            self.saldo += valor

    def mostrar_saldo(self):
        print(f"\nSaldo atual: R$ {self.saldo}.")

    def mostrar_dados_conta(self):
        print(f"Conta {self.num_conta} | {self.tipo_conta}")




