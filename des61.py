primeiro = int(input('Primeiro Termo:'))
razao = int(input('Razao:'))
cont = 1
while cont <= 10:
    print(primeiro, end=' ')
    primeiro += razao
    cont += 1
    print('- ' if cont <= 10 else '', end='')
