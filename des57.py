sexo = ''
while sexo != 'MF':
    sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()
    if sexo == 'M':
        print('Sexo masculino registrado com sucesso!')
    if sexo == 'F':
        print('Sexo feminino registrado com sucesso!')
    if sexo != 'MF':
        print('Dados invalidos. Por favor,', end= ' ')
