print('-='*20)
print('        ANALIZADOR DE TRIANGULO')
print('-='*20)
l1 = float(input('PRIMEIRO SEGUIMENTO:'))
l2 = float(input('SEGUNDO SEGMENTO:'))
l3 = float(input('TERCEIRO SEGMENTO:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
     print('formam um triangulo' , end=' ')
     if l1 == l2 == l3:
       print('EQUILATERO')
     elif l1 != l2 != l3 != l1:
       print('ESCALENO')
     else:
       print('ISOSCELES')
else:
 print('NAO FORMAM UM TRIANGULO')




