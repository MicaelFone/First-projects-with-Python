"""Imprima na tela a tabuada de um número inteiro lido
pelo teclado."""

numero=float(input("DIGITE O NÚMERO DA TABUADA:"))
contador=int(input("QUANTAS VEZES DESEJA QUE UM NÚMERO SEJA MULTIPLICADO:"))+1
for contador in range (contador):
    resultado=contador*numero
    print("RESULTADO DA TABUADA:",numero,"X",contador,"=",resultado)