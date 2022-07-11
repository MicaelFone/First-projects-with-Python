"""Dados três valores A, B, C, verificar se eles podem ser os
comprimentos dos lados de um triângulo e, se forem,
verificar se compõem um triângulo equilátero, isósceles ou
escaleno. Indicar também se estes valores não formam um
triângulo."""

lado_A=float(input("Digite o valor do lado do A:"))
lado_B=float(input("Digite o valor do lado do B:"))
lado_C=float(input("Digite o valor do lado do C:"))
if (lado_A+lado_B>lado_C):
    print("FORMA UM TRIÃNGULO")
else:
    print("NÃO FORMA UM TRIÃNGULO")
if lado_A==lado_B==lado_C:
    print("Triângulo Equilátero")
elif (lado_A==lado_B!=lado_C) or (lado_A==lado_C!=lado_B) or (lado_B==lado_C!=lado_A) :
    print(("Triangulo Isoceles"))
else:
    print(("Triangulo Escaleno"))

