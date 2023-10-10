print('='* 25)
print('   10 TERMOS DE UMA PA')
print('='* 25)
t = int(input('Primeiro termo:'))
r = int(input('Razao:'))
d = t + (9) * r + r
for c in range (t,d ,r):
    print(c, end= ' - ')
print('FIM')