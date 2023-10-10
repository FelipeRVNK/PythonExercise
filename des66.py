n = soma = cont =0
while True:
    n = int(input('digite um numero:'))
    if n == 999:
       break
    soma += n
    cont += 1
print(f'foram mostrados {cont} números, e a soma entre eles é vale {soma}!')