'''import math
n = float(input('digite um angulo qualquer : '))
seno = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print(f'Seno de {int(n)}, é {seno:.2f} \nCoseno é {cos:.2f} \nE sua tangente é {tan:.2f}')'''
from math import radians, sin, cos, tan
n = float(input('digite um angulo qualquer: '))
print(f'Seno de {int(n)}, é {sin(radians(n)):.2f} \nO cosseno é {cos(radians(n)):.2f}')
print(f'E sua tangente é {tan(radians(n)):.2f}')