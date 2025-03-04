def deposito(saldo, extrato):
    valor_deposito = int(input("Qual é o valor do depósito?: "))
    saldo = saldo + valor_deposito
    extrato["depositos"].append(valor_deposito)
    return saldo

def sacar(saldo, extrato):
    valor_saque = int(input("Qual é o valor do saque?: "))
    saldo = saldo - valor_saque
    extrato["saques"].append(valor_saque)
    return saldo

def exibir_extrato(saldo, extrato):
    print("Saldo: R$ {:.2f}".format(saldo))
    print("Depósitos: ")
    for i, valor in enumerate(extrato["depositos"]):
        print(f"{i + 1}. R$ {valor:.2f}")
    print("Saques: ")
    for i, valor in enumerate(extrato["saques"]):
        print(f"{i + 1}. R$ {valor:.2f}")

def main():
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
