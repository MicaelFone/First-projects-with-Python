""" Um vendedor de carros está com dificuldade em calcular sua
comissão a cada venda que realiza. Você irá ajudá-lo implementado
um programa capaz de, dado o valor da venda (valor do carro) e o
percentual da comissão, indicar quanto o vendedor ganhará.
– Exemplo:
• Valor da venda: 50.000,00 reais
• Comissão: 3%
• Ganho do vendedor: 1.500,00 reais
– PS: Obrigatório uso de função neste programa."""

global valor_da_comissao
valor_da_comissao=0.03

def valor_da_venda():
    global venda
    venda=float(input("DIGITE UM VALOR DA VENDA:"))
    return venda
valor_da_venda()

def comissao_recebida():
    global comissao
    comissao=venda*valor_da_comissao
    print("O VALOR A RECEBER DA VENDA É DE:","R$",comissao,"REAIS")
comissao_recebida()