# A variavél contador recebe 1.
soma = 1
# A variavéis para acumular a somas das notas e dos pesos digitados pelo usuario
nota = 0
peso = 0
acumula_nota = 0
acumula_peso = 0
# O usuário terá de decidir a quantidade de notas a serem emitidas.
quantidade_de_notas = int(input("Digite a quantidade de notas a serem emitidas:"))
quantidade_de_pesos = quantidade_de_notas
# Uso de um loop para sempre que o contador for menor ou igual a quantidade de notas a serem emitidas,então começa a calculadora.
while soma <= quantidade_de_notas:
    soma = soma + 1
# O usuário precisa digitar o valor da nota e do seu respectivo peso.
    nota = float(input("Digite o valor da nota:"))
    peso = int(input("Digite o valor do peso da nota:"))
# Uso de um loop,para sempre quando o usuário digitar uma nota inválida.
    while nota < 0 or nota > 10:
        print("NOTA INVÁLIDA!!!!!!!!!")
        nota = float(input("Digite novamente uma nova nota:"))
#As variavéis acumula_peso e acumula_nota  acabam tendo os seus valores incrementados
    acumula_peso +=peso
    acumula_nota += nota * peso
# Uso de um loop para verificar se o contador é maior do que a quantidade de notas então imprime a média final ponderada.
    while soma > quantidade_de_notas:
        resultado_final = acumula_nota / acumula_peso
        print("A MÉDIA FINAL PONDERADA É:",resultado_final)
        break