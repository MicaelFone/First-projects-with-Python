"""Implemente uma calculadora em Python capaz de
realizar as seguintes operações elementares envolvendo
inteiros:
– Somar dois valores;
– Dividir dois valores;
– Multiplicar dois valores;
– Subtrair dois valores;
• Todos os resultados devem ser impressos na tela (fora do módulo);
• Utilizar passagem de parâmetros."""

def inserir_valores():
    global valor_1
    valor_1= float(input("DIGITE UM VALOR O PARA PRIMEIRO O NÚMERO:"))
    global valor_2
    valor_2 = float(input("DIGITE UM VALOR O PARA SEGUNDO O NÚMERO:"))
    return valor_1
    return  valor_2
inserir_valores()

def soma():
    global valor_1
    global valor_2
    global resultado
    resultado=valor_1+valor_2
    return resultado

def subtracao():
    global valor_1
    global valor_2
    global resultado
    resultado=valor_1-valor_2
    return resultado

def multiplicacao():
    global valor_1
    global valor_2
    global resultado
    resultado=valor_1*valor_2
    return resultado

def divisao():
    global valor_1
    global valor_2
    global resultado
    resultado=valor_1/valor_2
    return resultado

def gerar_resultado():
    global resultado
    print("O RESULTADO DA OPERAÇÃO É:",resultado)

def menu():
    print("ESCOLHA UMA OPCAO VÁLIDA:")
    print("1-SOMA")
    print("2-SUBTRAÇÃO")
    print("3-DIVISÃO")
    print("4-MULTIPLICAÇÃO")
    print("5-DESLIGAR")
    opcao = int(input("SELECIONE A OPÇÃO DESEJADA:"))
    while opcao > 5 or opcao <= 0:
        opcao = int(input("SELECIONE NOVAMENTE UMA OPÇÃO VÁLIDA DESEJADA:"))
    if opcao==1:
        soma()
        gerar_resultado()
    if opcao==2:
        subtracao()
        gerar_resultado()
    if opcao==3:
        divisao()
        gerar_resultado()
    if opcao==4:
        multiplicacao()
        gerar_resultado()
    while opcao==5:
        break
menu()