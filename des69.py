cont18 = contW = contM = 0
continuar = ''
while True:
    print('='*31)
    print('     -CADASTRE UMA PESSOA-')
    print('='*31)
    idade = int(input('Idade:'))
    if idade >= 18:
        cont18 += 1
    sexo = str(input('Sexo: [M/F]')).upper().strip()
    if sexo == 'M':
        contM += 1
    if sexo == 'F' and idade < 20:
        contW += 1
    print('-'*31)
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo são {contM} homens cadastrados!')
print(f'E temos {contW} mulher com menos de 20 anos.')