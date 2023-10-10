print(' TABUADA DO FELIPE :)')
while True:
    n = int(input('quer ver a tabuada de qual valor? [número negativo para parar]'))
    if n < 0:
        break
    print('-'*15)
    for t in range(1,11):
        print(f'  {n} x {t} = {n * t}')
    print('-'*15)
print('Tabuada finalizada! Volte sempre! ')
