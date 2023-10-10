print('='*32)
print('     --BANCO DO FELIPERAS--')
print('='*32)
valor = int(input('Qual valor você quer sacar?'))
saque = valor
ced = 50
totced = 0
while True:
    if saque >= ced:
        saque -= ced
        totced += 1
    else:
        if totced != 0:
            print(f'total de {totced} cedulas de r${ced:.2f}')
        if saque < ced:
            ced = 20
        if saque < ced:
            ced = 10
        if saque < ced:
            ced = 1
        totced = 0
        if saque == 0:
            break
