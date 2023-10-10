num = int(input("digite um numero "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'A unidade desse numero é {u} \nSua dezena é {d} \nA centena {c} \nE o milhar é {m}')
