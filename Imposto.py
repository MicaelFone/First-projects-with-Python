"""Dado o saldo de uma conta corrente, verificar se este é
positivo ou negativo. Se negativo, imprimir o valor atual do
A tabela progressiva mensal do Imposto de Renda Retido
na Fonte estabelece as seguintes alíquotas (valores e
limites não atualizados):
– de R$ 1.257,13 até R$ 2.512,08,  alíquota de 15%
– acima de R$ 2.512,08,  alíquota de 27,5 %
• Escreva um algoritmo em Python que leia o salário de um
funcionário e calcule o valor do desconto."""

salario=float(input("DIGITE O VALOR DO SEU SALÁRIO BRUTO:"))
print("SEU SALÁRIO BRUTO FOI DE:",salario,"reais")
if salario==1257.13 or salario <= 2512.08:
    salario_aliquota=salario-(salario*0.15)
    print("SEU SALÁRIO LÍQUIDO FOI DE:",salario_aliquota,"reais")
if salario>=2512.08:
    salario_aliquota_2 = salario - (salario * 0.275)
    print("SEU SALÁRIO LÍQUIDO FOI DE:",salario_aliquota_2,"reais")