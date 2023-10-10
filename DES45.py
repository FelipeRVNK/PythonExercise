from random import randint
from time import sleep
print('''
[0] PEDRA 
[1] PAPEL
[2] TESOURA''')
escolha = int(input('qual a sua jogada?'))
itens = ('pedra','papel','tesoura')
pc = randint(0,2)
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('TESOURAA!!!')
sleep(1)
print('-='*20)
print(f'COMPUTADOR ESCOLHEU {itens[pc]}')
print(f'VOCE ESCOLHEU {itens[escolha]}')
print('-='*20)
if pc == 0: #pedra
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('VOCE GANHOU!')
    elif escolha == 2:
        print('VOCE PERDEU!')

elif pc == 1: #papel
    if escolha == 0:
        print('VOCE PERDEU!')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('VOCE GANHOU!')

elif pc == 2: #tesoura
    if escolha == 0:
        print('VOCE GANHOU!')
    elif escolha == 1:
        print('VOCE PERDEU!')
    elif escolha == 2:
        print('EMPATE')

