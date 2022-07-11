""" Um pesquisador mediu a altura de 30 crianças e anotou em uma tabela.
O seu objetivo é calcular a altura média das crianças,
além de identificar a altura da maior criança bem como da menor.
Sua tarefa é criar um programa em Python que ajude o pesquisador a realizar seu objetivo."""

def inserindo_uma_altura(criancas):
    alturas = []
    for inserir_alturas in range(criancas):
        altura=float(input("DIGITE A ALTURA DE UMA CRIANÇA:"))
        alturas.append(altura)
    print("ALTURAS:",alturas)
    return alturas

def somando_as_alturas(alturas):
    media=0
    soma=0
    for media_de_alturas in range(len(alturas)):
        soma=soma+alturas[media_de_alturas]
        media=soma/ len(alturas)
    return media

def maiores_que_media(alturas):
    maior=alturas[0]
    for alturas_acima_da_media in range(1,len(alturas)):
        if alturas[alturas_acima_da_media]>maior:
            maior = alturas[alturas_acima_da_media]
        return maior


def menores_que_media(alturas):
    menor = alturas[0]
    for alturas_abaixo_da_media in range(1,len(alturas)):
        if alturas[alturas_abaixo_da_media]< menor:
            menor = alturas[alturas_abaixo_da_media]
        return menor

estudantes=int(input("DIGITE A QUANTIDADE DE ESTUDANTES QUE DESEJA A CADASTRAR:"))
listas_de_alturas=inserindo_uma_altura(estudantes)
media=somando_as_alturas(listas_de_alturas)
maior=maiores_que_media(listas_de_alturas)
menor=menores_que_media(listas_de_alturas)

print("ALTURA ACIMA DA MÉDIA:",maior)
print("ALTURA ABAIXO DA MÉDIA:",menor)
print("A MÉDIA DE ALTURA DOS ESTUDANTES:",media)