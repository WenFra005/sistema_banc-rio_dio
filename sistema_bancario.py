def deposito(saldo, extrato):
    valor_deposito = input("Qual é o valor do depósito?: ")
    saldo = saldo + valor_deposito
    extrato.append(valor_deposito)
    return saldo

def sacar(saldo, extrato):
    valor_saque = input("Qual é o valor do saque?: ")
    saldo = saldo - valor_saque
    extrato.append(valor_saque)
    return saldo

def exibir_extrato(saldo, extrato):
    extrato_list = extrato
    print("Saldo: ", saldo)
    print(extrato_list)

def main():
    saldo = 0
    extrato = []
    while True:
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            saldo = deposito(saldo, extrato)
        elif opcao == "2":
            saldo = sacar(saldo, extrato)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            break
        else:
            print("Opção inválida")

main()
