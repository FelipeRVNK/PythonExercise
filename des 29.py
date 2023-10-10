v = float(input('qual a velociade do veiculo?'))
m = (v - 80)*7
if v>80:
    print(f'voce foi multado em R${m:.2f}!')
else:
    print('parabens voce esta em um a otima velocidade, continue assim!')