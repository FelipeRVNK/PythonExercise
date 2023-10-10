from random import randint
c = randint(0, 5)
print('-=-' * 20)
print('vou pensar em um numero de 0 a 5, Tente adivinhar...')
print('-=-' * 20)
r = int(input('que numero estou pensando?'))
if r == c:
    print('PARABENS VOCE ACERTOU!!!')
else:
    print(F'VOCE ERROU! Eu pensei no numero {c}.')