"""Dado um vetor de inteiros de 10 posições lido pelo teclado,
desenvolver um programa para localizar e imprimir na tela a posição
de um elemento qualquer, digitado pelo usuário. Caso o elemento não
esteja armazenado no vetor, imprimir "Não está no vetor" """
lista_numeros=[]
for contador in range(10):
  lista_numeros.append(float(input("INSIRA UM NÚMERO:")))
print(lista_numeros)
buscar_numero=float(input("DIGITE UM NÚMERO PARA BUSCAR:"))
if lista_numeros.count(buscar_numero)>=1:
  print("O NÚMERO BUSCADO ESTÁ NA POSIÇÃO:", lista_numeros.index(buscar_numero))
else:
  print("NÚMERO INVÁLIDO")