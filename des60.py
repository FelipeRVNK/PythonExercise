# in while ---
n = int(input('digite um numero:'))
cont = n + 1
f = 1
print(f'resultado de {n}! =', end='')
while cont != 1:
    cont -= 1
    f *= cont
    print(f' {cont}', end='')
    print(f' x' if cont > 1 else ' =', end= '')
print(f' {f}!', end='')

# in for ---
'''n = int(input('digite um numero:'))
f = 1
for c in range(n,0,-1):
    f *= c
    print(c, end=' ')
    print('x ' if c > 1 else '= ', end='')
print(f)'''
