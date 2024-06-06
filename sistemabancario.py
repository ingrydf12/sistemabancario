#desafio banco: depósito, saque e extrato.
''' DEPÓSITO
deve ser possível depositar valores POSITIVOS, armazenados em uma variável e exibidos na operação de extrato.


SAQUE
deve permitir realizar 3 saques diários com limite de 500 por saque. 

caso não tenha em conta, deve exibir a mensagem: não é possível sacar o dinheiro, ausência de saldo.

todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.

EXTRATO
listar todos os depósitos e saques realizados na conta

deve ser exibido ao final, o saldo atual da conta.
valores devem ser exibidos utilizando o formato R$ xxx.xx'''

menu = """MENU

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

"""
#declaracao
saldo = 0
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3 #const

#interacao menu
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. O depósito deve ser um valor maior que 0.")
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES: #primeira verificação
            print("Limite de saques diários atingido.")
        else:
            valor = float(input("Informe o valor do saque: R$ "))
            if valor > saldo:
                print("Não é possível sacar o dinheiro, ausência de saldo.\n")
            elif valor > limite:
                print("O valor do saque excede o limite permitido por saque (R$ 500,00).\n")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Valor inválido. O saque deve ser um valor positivo.")
    elif opcao == "e":
        print("\nExtrato:")
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")
    elif opcao == "q":
        break