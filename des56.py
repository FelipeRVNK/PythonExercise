i = 0
velho = 0
nomev = ''
cont = 0
for c in range(1,5):
    print(f'\033[36m===== {c}ª Pessoa =====')
    nome = str(input('\033[31mNome:')).upper().strip()
    idade = int(input('\033[31mIdade:'))
    i += idade
    sexo = str(input('\033[31mSexo [M/F]:')).upper().strip()
    if c == 1 and sexo == 'M':
        velho = idade
        nomev = nome
    if sexo == 'M' and idade > velho:
        velho = idade
        nomev = nome
    if sexo == 'F' and idade < 20:
        cont += 1
print(f'\033[39mA media de idade do grupo é de {i / 4:.0f} anos.')
print(f'\033[39mO homem mais velho tem {velho} e se chama {nomev}.')
print(f'\033[39mAo todo são {cont} mulheres menores de 20 anos.')
