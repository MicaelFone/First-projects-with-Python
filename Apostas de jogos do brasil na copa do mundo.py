"""Implemente um algoritmo em Python para permitir a aposta
de 5 jogadores em um bolão da Copa do Mundo. Cada
jogador indicará o resultado dos 3 primeiros jogos do
Brasil, no seguinte formato:
– Jogo 1: 2 x 0
– Jogo 2: 5 x 1
– Jogo 3: 3 x 0"""


jogadores=5
jogos=3
times=2
apostas=["0"]*jogadores

for jogador in range(jogadores):
    apostas[jogador]=["0"]*jogos
    for jogo in range(jogos):
        apostas[jogador][jogo]=["0"]*times

for jogador in range(jogadores):
    print("APOSTA DO JOGADOR",jogador,":")
    for jogo in range(jogos):
        print("APOSTA DO JOGO:", jogo)
        for time in range(times):
            print("NÚMEROS DE GOLS DA",time,"SELEÇÃO:")
            apostas[jogador][jogo][time]=int(input("DIGITE UM NÚMERO DE GOLS PARA ESTA SELEÇÃO:"))

print("APOSTAS DE TODOS OS JOGADORES PARA OS JOGOS PARA OS JOGOS DO BRASIL:",apostas)








