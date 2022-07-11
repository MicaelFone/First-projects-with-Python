""""Dado o exercício do cálculo da média, verificar se o
aluno está aprovado."""

nota_1=float(input("DIGITE O VALOR DA 1ºNOTA"))
nota_2=float(input("DIGITE O VALOR DA 2ºNOTA"))
nota_3=float(input("DIGITE O VALOR DA 3ºNOTA"))
media=(nota_1+nota_2+nota_3)/3
print("SUA MÉDIA É:",media)
if media >=7:
    print("APROVADO")
elif (media<7):
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")