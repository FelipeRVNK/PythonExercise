total = contmil = barato = cont = 0
nomebarato = ''
print('=' * 31)
print('     -LOJA SUPER BARATION-')
print('=' * 31)
while True:
    nome = str(input('Nome do produto:'))
    preço = float(input('Preço:'))
    cont += 1
    total += preço
    if preço > 1000:
        contmil += 1
    if cont == 1 or preço < barato:
        barato = preço
        nomebarato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    print('_'*31)
    if continuar == 'N':
        break
print(f'O preço total da compra foi de R${total:.2f}.')
print(f'Temos {contmil} produto custando mais de R$1000,00!')
print(f'O produto mais barato é {nomebarato} e custou R${barato:.2f}.')