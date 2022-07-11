"""Implementar um programa em Python para criar um vetor
para armazenar a altura de 5 pessoas. Em seguida
calcular a média dos 5 valores armazenados no vetor.
• Uma vez que a média foi calculada, imprimir na tela os
valores acima da média."""

alturas = []
somando_alturas = 0
for inserindo_as_alturas in range(5):
    alturas.append(float(input("DIGITE UMA ALTURA DE UMA PESSOA:")))
print("ALTURAS DOS CINCO ESTUDANTES:", alturas)

for contador in range(len(alturas)):
    somando_alturas += +alturas[contador]
media = somando_alturas / len(alturas)
print("A MÉDIA DE ALTURA DESTA TURMA FOI DE:", media)

for maior_altura in range(len(alturas)):
    if alturas[maior_altura] > media:
        print("AS ALTURAS ACIMA DA MÉDIA:", alturas[maior_altura])
