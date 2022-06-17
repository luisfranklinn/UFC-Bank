class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        


    def mostrar_dados_cliente(self):
        print ('\nDados da Conta')
        print(f"\nNome: {self.nome} \nCPF: {self.cpf} \nIdade: {self.idade}")


