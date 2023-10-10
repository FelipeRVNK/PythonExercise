cont = 0
cont1 = 0
for c in range(1,3):
    idade = int(input(f'Em que ano nasceu a {c}ª pessoa?'))
    if idade > 2005:
        cont += 1
    elif idade <= 2005:
        cont1 += 1
print('\033[36m='*25,)
print(f'\033[33mTemos {cont} menores de idade! \nE {cont1} maiores de idade!')
print('\033[36m='*25)
