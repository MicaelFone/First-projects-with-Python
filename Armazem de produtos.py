"""Um armazém trabalha com 100 mercadorias diferentes identificadas
pelos números inteiros de 1 a 100. O dono do armazém anota a
quantidade de cada mercadoria vendida durante o mês. Ele tem uma
tabela que indica para cada mercadoria o preço de venda. Escreva o
algoritmo para calcular o faturamento mensal do armazém, isto é:
– faturamento = Quantidade * preço """
lucros=[]
for contador in range(2):
    custo=float(input("DIGITE O PRECO DESSE PRODUTO:"))
    quantidade=float(input("DIGITE A QUANTIDADE DESSE PRODUTO:"))
    lucro=custo*quantidade
    lucros.append(lucro)
print("FATURAMENTO MENSAL DO ARMAZÉM:","R$",sum(lucros),"REAIS")