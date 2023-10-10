soma = 0
for c in range (1,7,1):
    n = int(input('digite um numero'))
    if n % 2 == 0:
        soma = soma + n
print(f'A soma dos numeros pares é {soma}.')