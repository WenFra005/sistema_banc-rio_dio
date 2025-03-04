# Sistema Bancário em Python

Este repositório contém um sistema bancário simples implementado em Python. O sistema permite que o usuário realize operações básicas como depósitos, saques e exibição do extrato da conta.

## Funcionalidades

- **Depósito**: Permite ao usuário adicionar um valor ao saldo da conta.
- **Saque**: Permite ao usuário retirar um valor do saldo da conta, desde que haja saldo suficiente.
- **Extrato**: Exibe um extrato detalhado das operações realizadas, incluindo depósitos, saques e o saldo atual.

## Estrutura do Código

O código está organizado em funções principais:

- `depositar(saldo, extrato)`: Realiza um depósito na conta.
- `sacar(saldo, extrato)`: Realiza um saque na conta.
- `exibir_extrato(saldo, extrato)`: Exibe o extrato da conta.
- `main()`: Função principal que gerencia o fluxo do programa.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o script `sistema_bancario.py` utilizando o comando:
   ```sh
   python sistema_bancario.py