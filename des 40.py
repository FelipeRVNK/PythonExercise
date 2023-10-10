n1 = float(input('primeira nota:'))
n2 = float(input('segunda nota:'))
media = (n1 + n2) / 2
if media <= 5.0:
 print(f'sua media é {media}, VOCÊ ESTÁ REPROVADO!')
elif media >= 5 and media <7:
    print(f'sua media é {media} VOCE FICOU PARA RECUPERAÇAO!')
else:
    print(f'VOCE FOI APROVADO! Sua media é {media}')

