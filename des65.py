resposta = ''
cont = total = maior = menor = 0
while resposta != 'N':
    numero = int(input('digite um numero:'))
    total += numero
    cont += 1
    resposta = str(input('quer continuar? [S/N]')).upper().strip()
    if cont == 1:
        maior = menor = numero
    else:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
print(f'Você digitou {cont} números e a médias entre eles é {total/cont:.2f}!')
print(f'O maior número é {maior} e o menor é {menor}.')