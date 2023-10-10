d = float(input('qual a distancia da viagem em km?'))
if d <= 200:
    print(f'o valor da sua passagem é de R${d * 0.50:.2f}')
else:
    print(f'o valor da sua passagem é de R${d * 0.45:.2f}')
