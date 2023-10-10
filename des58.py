import emoji
from random import randint
palpite = ''
cont = 0
c = randint(0,10)
print(emoji.emojize('===== Sou seu computador =====\n:eyes: Acabei de pensar em um número de 0 a 10 :eyes:'))
while palpite != c:
    palpite = int(input('Qual seu palpite?'))
    cont += 1
    if palpite == c:
        print(emoji.emojize(f'\033[36m:fireworks:PARABENS!!! Você acertou com {cont} tentativas.:fireworks:'))
    if palpite != c and palpite > c:
        print('Menos... Tente novamente', end= ' ')
    if palpite != c and palpite < c:
        print('Mais... Tente novamente', end= ' ')
