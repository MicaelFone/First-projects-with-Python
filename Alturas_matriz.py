notas=[]
numero_de_linhas=4
numero_de_colunas=3
soma=0
notas=["0"]*numero_de_linhas

for linha in range(numero_de_linhas):
    notas[linha]=["0"]*numero_de_colunas

for linha in range(numero_de_linhas):
    for coluna in range(numero_de_colunas):
        notas[linha][coluna]=float(input("INSIRA UMA NOTA DE UM ALUNO:"))

for linha in range(numero_de_linhas):
    for coluna in range(numero_de_colunas):
        soma+=notas[linha][coluna]
    media=soma/numero_de_colunas
    print("A MÉDIA DE NOTAS DOS ALUNOS DA TURMA FOI DE:",media)
    break