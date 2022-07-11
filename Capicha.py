"""Implementar um programa em Python capaz de gerar um Captcha e
permitir sua avaliação.
• Detalhes
– O programa deverá ser capaz de gerar um captcha de 6 caracteres. O captcha
obrigatoriamente deve conter letras (a-z) e números (0-9).
– Após sua geração, o programa deve permitir a leitura de um conjunto de caracteres
pelo teclado e a comparação com o captcha anteriormente gerado."""

import random
acertos=0
capicha=[]
global contador
contador=0
def gerar_capicha():
    global contador
    while contador <3:
        gerar_letras = chr(random.randint(ord('a'), ord('z')))
        capicha.append(gerar_letras)
        gerar_number = chr(random.randint(ord('0'), ord('9')))
        str(gerar_number)
        capicha.append(gerar_number)
        contador+=1
    print("CAPICHA:",capicha)

gerar_capicha()

def verificar_capicha():
    for contador in range(6):
        global verificador_capicha
        verificador_capicha=0
        verificador_capicha = input("DIGITE UM CHARACTER PARA VERIFICAR SE VOCE É UM RÔBO OU NÃO É:")
verificar_capicha()




def validar_capicha():
    global acertos
    global verificador_capicha
    for verificador in range(len(capicha)):
        if capicha[verificador]==verificador_capicha:
            acertos+=+1
    if acertos<1:
        print("CAPICHA INVÁLIDO.")
    while acertos==1:
        print("CAPICHA VÁLIDO.")
        break
validar_capicha()


