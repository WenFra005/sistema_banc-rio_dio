def deposito(saldo, extrato):
    valor_deposito = input("Qual é o valor do depósito?: ")
    saldo = saldo + valor_deposito
    extrato.append(valor_deposito)
    return saldo

def sacar(saldo):
    valor_saque = input("Qual é o valor do saque?: ")
    saldo = saldo - valor_saque
    return saldo