tot = 0
n = int(input('digite um numero:'))
for c in range(1, n + 1, 1):
    if n % c == 0:
        tot += 1
if tot == 2:
    print('número primo!'.upper())
else:
    print('nao é um número primo!'.upper())
