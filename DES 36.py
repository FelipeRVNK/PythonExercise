casa = float(input('qual o valor da casa?'))
salario = float(input('qual é o seu salario?'))
anos = int(input('quantos anos de finaciamento?'))
prestaçao = casa / (anos * 12)
minimo = salario * 30/100
print(f'o valor da prestaçao é de {prestaçao:.2f} e')
print(f'os 30% de seu salario  é de {minimo:.2f}')
if prestaçao <= minimo:
    print('emprestimo pode ser CONCEDIDO!')
else:
    print('emprestimo NEGADO!')