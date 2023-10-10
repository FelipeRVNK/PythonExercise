ano = int(input('digite o ano de nascimento:'))
if ano > 2005:
    print(f'quem nasceu em {ano} tem {2023 - ano} anos em 2023')
    print(f'ainda faltam {ano - 2005} para o alistamento ')
    print(f'seu alistamento sera em {(ano - 2005) + 2023}')
elif ano < 2005:
    print(f'quem nasceu em {ano} tem {2023 - ano} anos em 2023')
    print(f'voce ja deveria ter se alistado há {2005 - ano} anos')
    print(f'seu alistamento foi em {2023 - (2005-ano)}')
else:
    print(f'quem nasceu em {ano} tem {2023 - ano} anos em 2023')
    print('voce deve se alistar IMEDIATAMENTE SUA MULA CABEÇA DE PIKA! Ou devera pagar uma multa!')