"""
Esse programa simula um sistema bancário simples, permitindo que o usuário faça depósitos, saques e exiba o extrato da conta.
"""
def depositar(saldo, extrato):
    """
    Realiza um depósito na conta.

    Args:
        saldo (float): O saldo atual da conta.
        extrato (dict): O extrato da conta contendo listas de depósitos e saques.

    Returns:
        float: O novo saldo após o depósito.
    """
    valor_deposito = int(input("Qual é o valor do depósito?: "))
    saldo = saldo + valor_deposito
    extrato["depositos"].append(valor_deposito)
    print("Depósito efetuado com sucesso\n")
    return saldo

def sacar(saldo, extrato):
    """
    Realiza um saque na conta.

    Args:
        saldo (float): O saldo atual da conta.
        extrato (dict): O extrato da conta contendo listas de depósitos e saques.

    Returns:
        float: O novo saldo após o saque, ou o saldo atual se o saque não for possível.
    """
    valor_saque = int(input("Qual é o valor do saque?: "))
    if valor_saque <= saldo:
        saldo = saldo - valor_saque
        extrato["saques"].append(valor_saque)
    else:
        print("Saldo insuficiente\n")
    return saldo

def exibir_extrato(saldo, extrato):
    """
    Exibe o extrato da conta, incluindo depósitos, saques e o saldo atual.

    Args:
        saldo (float): O saldo atual da conta.
        extrato (dict): O extrato da conta contendo listas de depósitos e saques.
    """
    print("------Extrato------")
    print("---Depósitos---")
    for i, valor in enumerate(extrato["depositos"]):
        print(f"{i + 1}. R$ {valor:.2f}")
    print("---Saques---")
    for i, valor in enumerate(extrato["saques"]):
        print(f"{i + 1}. R$ {valor:.2f}")
    print("-------------------")
    print(f"Saldo: R$ {saldo:.2f}")
    print("\n")


def main():
    """
    Função principal que gerencia o fluxo do programa de operações bancárias.
    """
    saldo = 0
    extrato = {
        "depositos": [],
        "saques": []
    }
    while True:

        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            saldo = depositar(saldo, extrato)
        elif opcao == "2":
            saldo = sacar(saldo, extrato)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            break
        else:
            print("Opção inválida")

main()
