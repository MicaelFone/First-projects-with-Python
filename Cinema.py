# Um cinema possui um programa de fidelidade que oferece
# descontos para os clientes mais assíduos. Implemente um
# programa em Python para calcular quanto alguém deve pagar pela
# entrada do cinema, sabendo-se:

numero_de_entradas=int(input("DIGITE O NÚMERO DE ENTRADAS PARA ASSISTIR ESTE FILME QUE VOCE DESEJA:"))
ticket_inteira=50.00
total_pago=0
for desconto in range(numero_de_entradas):
    print("-INFORME O TIPO DE DESCONTO:")
    print("1-ESTUDANTE(50%)")
    print("2-IDOSO(100%)")
    print("3-SEM DESCONTO(0%)")
    desconto=int(input("DIGITE O DESCONTO ESCOLHIDO:"))
    while desconto>3 or desconto <=0:
        desconto = int(input("DIGITE O NOVAMENTE SEU DESCONTO ESCOLHIDO:"))
    if desconto==1:
        ingresso=ticket_inteira*0.5
        total_pago+=+ingresso
        print("O PREÇO DESTE TICKET:","R$",ingresso,"REAIS")
    if desconto==2:
        ingresso=ticket_inteira*0.0
        total_pago+=+ingresso
        print("O PREÇO DESTE TICKET:", "R$", ingresso, "REAIS")
    if desconto==3:
        ingresso=ticket_inteira
        total_pago+=+ingresso
        print("O PREÇO DESTE TICKET:", "R$", ingresso, "REAIS")

print("POR FAVOR UMA OPÇAO VÁLIDA:")
print("1-TICKET DO ESTACIONAMENTO")
print("2-SEM TICKET DO ESTACIONAMENTO")
opcao=int(input("DIGITE UMA OPÇÃO VÁLIDA PARA O ESTACIONAMENTO:"))

if opcao==1:
    quantidade_de_horas=float(input("DIGITE A QUANTIDADE DE HORAS DESEJADAS:"))
    preco_do_estacionamento=quantidade_de_horas*12
    print("VALOR DO TICKET DO ESTACIONAMENTO:","R$",preco_do_estacionamento,"REAIS")
    print("TOTAL DA COMPRA:","R$",preco_do_estacionamento+total_pago,"REAIS")
if opcao==2:
    print("TOTAL DA COMPRA:", "R$",total_pago,"REAIS")


