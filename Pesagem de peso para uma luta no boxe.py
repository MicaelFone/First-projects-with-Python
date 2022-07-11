"""Escreva um algoritmo que dado o peso de um boxeador,
informe a categoria a qual ele pertence, seguindo a tabela
abaixo:
Categoria Peso (Kg)
Palha Menor que 50 Kg
Pluma 50 - 59,99
Leve 60 - 75,99
Pesado 76 - 87,99
Super Pesado Maior que 88 Kg"""

peso=float(input("DIGITE SEU PESO PARA DESCOBRIR EM QUAL CATEGORIA SE CAIXA:"))
if peso < 50:
    print("PESO PALHA")
if (peso>=50 and peso<=59.99):
    print("PESO PLUMA")
if (peso>=60 and peso<=75.99):
    print("PESO LEVE")
if (peso>=76 and peso<=87.99):
    print("PESO PESADO")
if peso > 88:
    print("PESO SUPERPESADO")
