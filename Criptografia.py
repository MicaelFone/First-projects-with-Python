"""Implemente um programa em Python para criptografar palavras (lidas
pelo teclado) utilizando a seguinte estratégia: cada letra da palavra
original será modificada por outra letra, como segue:
– Original  Criptografia
A D
B E
C F
D G
E H
...
X A
Y B
Z C
– Imprimir na tela a palavra criptografada."""

alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def descobirir_palavra():
    palavra_criptografada=""
    palavra=input("DIGITE UMA PALAVRA A SER CODIFICADA:")
    for letra in palavra:
        for contador in range(len(alfabeto)):
            if letra==alfabeto[contador]:
                if contador <=22:
                    palavra_criptografada+=alfabeto[contador+3]
                else:
                    palavra_criptografada += alfabeto[contador+3-27]
    print(palavra_criptografada)
descobirir_palavra()