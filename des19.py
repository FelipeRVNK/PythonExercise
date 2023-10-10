from random import choice
p = input('qual é o primeiro aluno? ')
s = input('qual é o segundo aluno? ')
t = input('qual é o terceiro aluno? ')
q = input('qual é o quarto aluno?')
lista = [p, s, t, q]
e = choice(lista)
print(f'O escolhido é {e}')
