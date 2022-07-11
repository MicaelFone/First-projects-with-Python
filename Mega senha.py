"""Implemente um programa em Python para verificar quantos
números uma aposta acertou na Megasena. O programa deve ler do
teclado os 6 números sorteados e comparar com 6 números
apostados."""
from random import randrange
numeros_sorteados=[]
numeros_apostados=[]
acertos=0
contador=0

while contador<6:
    sorteio=randrange(1,61)
    if sorteio in numeros_sorteados:
        pass
    else:
        numeros_sorteados.append(sorteio)
    contador+=+1

for apostando in range(6):
    aposta=int(input("APOSTE UM NÚMERO:"))
    while aposta in numeros_apostados:
        print("POR FAVOR INSIRA NOVAMENTE UM NÚMERO VÁLIDO")
        aposta = int(input("APOSTE UM NÚMERO NOVAMENTE QUE NÃO SEJA REPETIDO:"))
    numeros_apostados.append(aposta)

numeros_apostados.sort()
numeros_sorteados.sort()
print("SORTEIO:",numeros_sorteados)
print("SUA APOSTA É:",numeros_apostados)


for sorteio in range(len(numeros_sorteados)):
    for aposta in range(len(numeros_apostados)):
        if numeros_sorteados[sorteio]==numeros_apostados[aposta]:
            acertos+=+1
print("VOCÊ TEVE:",acertos,"ACERTOS")

if numeros_apostados.count(sorteio)==6:
    print("VOCÊ ACERTOU UMA QUADRA COMPLETA")
