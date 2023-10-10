from math import hypot
a = float(input('qual o valor do cateto adjacente:'))
o = float(input('qual o valor do cateto oposto:'))
print(f' a hipotenusa vai medir {hypot(a,o):.2f}')
