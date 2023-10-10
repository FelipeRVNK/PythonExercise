print('-' *30)
print('  - Sequência de Fibonacci -')
print('-' *30)
termo = int(input('quantos termos voce quer mostrar?'))
n1 = 0
n2 = 1
soma = 0
cont = 2
print(f'{n1} - {n2}', end=' - ')
while cont != termo:
    soma = n1 + n2
    print(f'{soma}', end=' - ')
    cont += 1
    n1 = n2
    n2 = soma
print('FIM')
