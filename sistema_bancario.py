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

def extrato(saldo, extrato):
    extrato_list = extrato
    print("Saldo: ", saldo)
    print(extrato_list)