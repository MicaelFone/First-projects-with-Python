"""Implemente um algoritmo em Python capaz de ler 5 inteiros do teclado e
imprimir na tela o maior número digitado. Dica: você vai precisar utilizar o while e
o if neste exercício."""
contador=0
numero=[]
for contador in range(5):
    numero.append(float(input("DIGITE UM NÚMERO:")))
print("O",max(numero),"É O MAIOR NÚMERO.")
