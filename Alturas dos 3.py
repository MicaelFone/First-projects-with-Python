"""Anacleto tem 1,50 metro e cresce 2 centímetros por
ano, enquanto Felisberto tem 1,10 metro e cresce 3
centímetros por ano. Construa um algoritmo em Python
que calcule e mostre quantos anos serão necessários para
que Felisberto seja maior que Anacleto."""

Anacleto = 1.5
Felisberto = 1.1
contador_de_anos = 0

while Anacleto>Felisberto:
    Anacleto = Anacleto + 0.2
    Felisberto = Felisberto+ 0.3
    contador_de_anos+=+1
print("DEMORARÁ",contador_de_anos,"ANOS PARA QUE FELISBERTO SEJA MAIOR QUE ANACLETO.")