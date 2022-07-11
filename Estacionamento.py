"""Implementar um programa contendo um
procedimento em Python para calcular o valor que deve ser pago por uma pessoa que deixa seu
carro estacionado por X horas em um
estacionamento que cobra Y reais por hora. O
procedimento deve receber os valores X e Y via argumentos."""
preco=15.00
def calcular_o_valor_do_estacionamento(horas,preco):

    total_do_estacionamento=horas*preco
    print("O VALOR TOTAL DO ESTACIONAMENTO:",total_do_estacionamento)
horas=int(input("DIGITE O NUMERO DE MINUTOS:"))
preco=float(input("DIGITE O NÚMERO DE HORAS:"))