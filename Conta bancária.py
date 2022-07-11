"""Dado o saldo de uma conta corrente,
verificar se este é positivo ou negativo. Se negativo, imprimir o valor atual do saldo"""
"""Implemente um programa em Python para controlar a 
conta bancária de uma pessoa, permitindo algumas 
operações básicas como:
– Criar a conta (com a definição do saldo inicial);
– Depósito;
– Retirada (somente se houver saldo);
– Impressão do saldo."""


def criar_conta():
    global saldo
    saldo=float(input("DIGITE O SEU SALDO INICIAL:"))
    return saldo
criar_conta()
def depositar():
    depositar=float(input("INSIRA UM VALOR DE DEPÓSITO:"))
    global saldo
    saldo+=depositar
    return saldo

def saque():
    global saldo
    if saldo >0:
        saque=float(input("INSIRA UM VALOR DE SAQUE:"))
        saldo-=saque
    else:
        print("NÃO É POSSÍVEL FAZER UM SAQUE.")
    return saldo

def imprimir():
    global saldo
    print("O SEU SALDO TOTAL É DE:","R$",saldo,"REAIS")
    return saldo

def limite_bancario():
    limite_de_credito=float(input("DIGITE O SEU LIMITE DE CRÉDITO ESPECIAL:"))
    global saldo
    if saldo ==0:
        print("SUA CONTA ESTÁ ZERADA")
    if saldo>0:
        print("SEU SUA CONTA POSSUI UM CRÉDITO DE:","R$",saldo,"REAIS")
    if (saldo <0) and (saldo > limite_de_credito):
        print("SEU SUA CONTA POSSUI ESTÁ COM UM DÉBITO DE:","R$",saldo,"REAIS")
    if (saldo <0) and (saldo < limite_de_credito):
        print("SEU SUA CONTA POSSUI ESTÁ COM UM DÉBITO E ESTÁ NO CHEQUE ESPECIAL DE:","R$",saldo,"REAIS")

def menu_secundario():
    print("ESCOLHE UMA OPCAO VÁLIDA:")
    print("1-VOLTAR AO MENU PRINCIPAL")
    print("2-IMPRIMIR O SALDO BANCÁRIO")
    opcao_de_retorno=float(input("DIGITE UMA OPÇÃO VÁLIDA:"))
    while opcao_de_retorno>2 or opcao_de_retorno<=0:
        opcao_de_retorno = int(input("SELECIONE NOVAMENTE UMA OPÇÃO VÁLIDA DESEJADA:"))
    if opcao_de_retorno==1:
        menu_inicial()
    if opcao_de_retorno==2:
        imprimir()
        menu_inicial()

def menu_inicial():
    print("ESCOLHA UMA OPÇÃO DESEJADA:")
    print("1-DEPÓSITO")
    print("2-SAQUE ")
    print("3-VERIFICAR O LIMITE BANCÁRIO")
    print("4-IMPRIMIR O SALDO BANCÁRIO")
    opcao=int(input("SELECIONE A OPÇÃO DESEJADA:"))
    while opcao>4 or opcao<=0:
        opcao = int(input("SELECIONE NOVAMENTE UMA OPÇÃO VÁLIDA DESEJADA:"))
    if opcao==1:
        depositar()
        menu_secundario()
    if opcao==2:
        saque()
        menu_secundario()
    if opcao==3:
        limite_bancario()
        menu_secundario()
    if opcao==4:
        imprimir()
        menu_inicial()

menu_inicial()
