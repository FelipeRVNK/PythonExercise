from random import randint
cont = 0
print('='*26)
print('VAMOS JOGAR PAR OU IMPAR')
print('='*26)
while True:
    escolhapc = randint(1, 10)
    valorplayer = int(input('Digite um valor:'))
    escolha = str(input('Você quer PAR ou IMPAR? [P/I]')).upper().strip()
    soma = valorplayer + escolhapc
    if soma % 2 == 0:
        print(f'voce jogou {valorplayer} e o computador jogou {escolhapc}. Total deu {soma} DEU PAR!')
        if escolha == 'P':
            print('VOCE GANHOU! Vamos de novo...')
            cont += 1
        if escolha == 'I':
            print('VOCE PERDEU!')
            print('=' * 32)
            break
    else:
        print(f'voce jogou {valorplayer} e o computador jogou {escolhapc}. Total deu {soma} DEU IMPAR!')
        if escolha == 'P':
            print('VOCE PERDEU!')
            print('=' * 32)
            break
        if escolha == 'I':
            print('VOCE GANHOU! Vamos de novo...')
            cont +=1
print(f'GAME OVER!  Você ganhou {cont} vezes!')
print('=' * 32)
