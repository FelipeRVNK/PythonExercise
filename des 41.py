from datetime import date
atual = date.today().year
ano = int(input('DIGITE O ANO QUEM QUE NASCEU:'))
idade = atual - ano
if idade <= 9:
    print('O atleta é MIRIM')
elif idade <= 14:
    print('O atleta é INFANTIL')
elif idade <= 19:
    print('O atleta é JUNIOR')
elif idade <= 25:
    print('O atleta é SENIOR')
else:
    print('O atleta é MASTER')