n = 0
cont = 0
total = 0
while n != 999:
    total += n
    n = int(input('Digite um número [Digite 999 para parar]:'))
    if n != 999:
        cont += 1
    elif n == 999:
        print(f'Você digitou {cont} números e a soma entre eles é {total}!')
