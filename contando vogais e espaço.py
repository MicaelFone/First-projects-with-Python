"""Implemente um programa em Python que seja capaz
de criar uma stringe imprimir na tela:
– quantas vezes foram encontradas as letras vogais;
– quantos espaços existem no texto."""

contando_vogais=0
contando_espaco=0
palavra=input("ESCREVA UMA PALAVRA:")
for contador in range(len(palavra)):
  if palavra[contador]==" ":
    contando_espaco+=+1
  if palavra[contador]=="a"or palavra[contador]=="A" or palavra[contador]=="E" or palavra[contador]=="e" or palavra[contador]=="I" or palavra[contador]=="i" or palavra[contador]=="O" or palavra[contador]=="o" or palavra[contador]=="u" or palavra[contador]=='U':
    contando_vogais+=+1
print("A QUANTIDADE DE ESPAÇOS ENCONTRADOS:",contando_espaco)
print("A QUANTIDADE DE VOGAIS ENCONTRADAS:",contando_vogais)