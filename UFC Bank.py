from class_conta import Conta
from class_cliente import Cliente
import random


#Usuario Cadastrado
nome = "Guilherme Frutuoso de Almeida"
idade = 22
cpf = "381.504.160-05"
num_conta = 1
saldo = 120
tipo_conta = "Poupança"
senha_conta = "123456"
usuario_0 = Cliente(nome, cpf, idade)
conta_0 = Conta(usuario_0, num_conta, saldo, tipo_conta,senha_conta)


def cadastrar_cliente():
# Cadastro Cliente
    global usuario_1
    global conta_1

    letras_cadastradas = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")

    nome = str(input("Informe o seu nome: "))
    valida_nome = set((nome))
    while valida_nome.issubset(letras_cadastradas) != True:
        print("!!NOME INVÁLIDO!!\n!!Insira apenas letras!!")
        nome = str(input("Informe o seu nome: "))
        valida_nome = set((nome))

    idade = int(input(f"Ótimo sr(a) {nome}, agora me informe sua idade: "))
    while idade < 18:
        print("Infelizmente menores de idade não podem se cadastrar no banco")
        idade = int(input("Insira um idade válida: "))


    cpf = str(input("Informe o CPF: "))
    valida_cpf = cpf.isdigit()
    while len(cpf) != 11 or valida_cpf != True:
        print("!!CPF INVÁLIDO!!")
        cpf = str(input("Informe um CPF com 11 dígitos: "))
        valida_cpf = cpf.isdigit()


    escolha = int(input("\n"'''Escolha o tipo da sua conta?
        1 - Corrente
        2 - Poupança
    Opção: '''))

    while escolha != 1 and escolha != 2:
        print("!!OPÇÃO INVÁLIDA!!")
        escolha = int(input("\n"'''Escolha o tipo da sua conta?
        1 - Corrente
        2 - Poupança
    Opção: '''))

    if escolha == 1:
        tipo_conta = "Corrente"
    else:
        tipo_conta = "Poupança"

    senha_conta = str(input("Cadastre uma senha númerica de 6 dígitos: "))
    valida_senha = senha_conta.isdigit()
    while len(senha_conta) != 6 and valida_senha != True:
        print("!!SENHA INVÁLIDA!")
        senha_conta = str(input("Informe um CPF com 11 dígitos: "))
        valida_senha = senha_conta.isdigit()

    num_conta = random.randint(2,300)
    saldo = 0
    usuario_1 = Cliente(nome, cpf, idade)
    conta_1 = Conta(usuario_1, num_conta, saldo, tipo_conta, senha_conta)
    menu(usuario_1, conta_1)

def menu(usuario, conta):
    while True:
        opcao = int(input("\n"f'''Seja bem-vindo(a) {usuario.nome} | Conta {conta.num_conta}
        O que deseja fazer?
            1 - Saque
            2 - Depósito
            3 - Saldo
            4 - Realizar transferência
            5 - Meus Dados
            6 - Trocar de Conta
            7 - Sair
            
        Opção: '''))
        if opcao < 1 or opcao > 7:
            print('Opção invalida, digite um número entre 1 e 7\n')

        match opcao:   
            case 1: # Saca o dinheiro da Conta
                valor = int(input(f"Quanto deseja sacar do seu saldo de {conta.saldo}? "))
                conta.saque(valor)

                
            case 2: # Deposita o dinheiro da Conta
                valor = int(input(f"Quanto deseja depositar? "))
                conta.deposito(valor)


            case 3: # Mostra o Saldo da Conta
                conta.mostrar_saldo()


            case 4: # Transferência Bancária
                conta_a_transferir = int(input(f"Para qual conta você deseja transferir?: "))
                while True:
                    if conta_a_transferir != conta_0.num_conta and conta_a_transferir != conta_1.num_conta:
                        print("!!CONTA NÃO ENCONTRADA!!")
                        conta_a_transferir = int(input("Para qual conta deseja transferir: "))

                    elif conta_a_transferir == conta_0.num_conta and conta_a_transferir == conta_1.num_conta:
                        if conta_a_transferir == conta:
                            print("!!VOCÊ NÃO PODE TRANSFERIR PARA SUA PRÓPRIA CONTA!!")
                            conta_a_transferir = int(input(f"Para qual conta você deseja transferir?: "))

                    break
                

                valor = int(input(f"Quanto deseja transferir do seu saldo de R${conta.saldo}? "))

                entrada_senha = str(input("Insira sua senha para confirmar a transferência: "))
                while entrada_senha != conta.senha_conta:
                    print("!!SENHA INVÁLIDA!!")
                    entrada_senha = str(input("Insira sua senha para confirmar a transferência: "))


                if conta_a_transferir == conta_0.num_conta:
                    conta_0.deposito_transf(valor)
                    conta_1.saque_transf(valor)
                    print(f"Transferencia de {valor} para a conta {conta_a_transferir} realizada com sucesso!")
                    conta.mostrar_saldo()
                else:
                    conta_0.saque_transf(valor)
                    conta_1.deposito_transf(valor)
                    print(f"Transferencia de {valor} para a conta {conta_a_transferir} realizada com sucesso!")
                    conta.mostrar_saldo()


            case 5: # Mostra os Dados do Cliente
                usuario.mostrar_dados_cliente()
                conta.mostrar_dados_conta()


            case 6: # Trocar de Conta
                entrada_conta = int(input("Insira sua conta: "))
                while entrada_conta != conta_0.num_conta and entrada_conta != conta_1.num_conta:
                    print("!!CONTA NÃO ENCONTRADA!!")
                    entrada_conta = int(input("Insira sua conta: "))

                entrada_senha = str(input("Insira sua senha: "))
                while entrada_senha != conta_0.senha_conta and entrada_senha != conta_1.senha_conta:
                    print("!!SENHA INVÁLIDA!!")
                    entrada_senha = str(input("Insira sua senha: "))

                if entrada_conta == conta_1.num_conta:
                    usuario = usuario_1
                    conta = conta_1
                else:
                    usuario = usuario_0
                    conta = conta_0

                menu(usuario,conta)      
                break          


            case 7: # Sai do Programa
                print("Obrigado! Até a próxima.")
                break



# INICIAL DO PROGRAMA
escolha = int(input("\n"'''Seja bem vindo ao UFC Bank, o que você deseja fazer?
    1 - Abrir Conta
    2 - Entrar
Opção: '''))

while escolha != 1 and escolha != 2:
    print("!!OPÇÃO INVÁLIDA!!")
    escolha = int(input("\n"f'''o que você deseja fazer?
    1 - Abrir Conta
    2 - Entrar
Opção: '''))

if escolha == 1:
    cadastrar_cliente()
else:
    entrada_conta = int(input("Insira sua conta: "))
    while entrada_conta != conta_0.num_conta:
        print("!!CONTA NÃO ENCONTRADA!!")
        entrada_conta = int(input("Insira sua conta: "))
    

    entrada_senha = str(input("Insira sua senha: "))
    while entrada_senha != conta_0.senha_conta:
        print("!!SENHA INVÁLIDA!!")
        entrada_senha = str(input("Insira sua senha: "))
    

    menu(usuario_0, conta_0)