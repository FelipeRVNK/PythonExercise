import emoji
from time import sleep
print('\033[37m===== CALCULADORA DO FELIPE =====')
n1 = int(input('digite um número:'))
n2 = int(input('digite outro número:'))
escolha = 0
while escolha != 7:
    print(("""    \033[32m[ 1 ] SOMAR
    \033[33m[ 2 ] SUBTRAIR
    \033[31m[ 3 ] MULTIPLICAR
    \033[35m[ 4 ] DIVIDIR
    \033[34m[ 5 ] QUEM É MAIOR
    \033[36m[ 6 ] NOVOS NÚMEROS
    \033[37m[ 7 ] SAIR DO PROGRAMA"""))
    escolha = int(input('\033[38m>>> Qual sua opçao?'))
    if escolha == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
    elif escolha == 2:
        print(f'A subitraçao entre {n1} - {n2} é {n1-n2}')
    elif escolha == 3:
        print(f'A multiplicaçao entre {n1} x {n2} é {n1*n2}')
    elif escolha == 4:
        print(f'A divisao entre {n1} / {n2} é {n1/n2:.2f}')
    elif escolha == 5:
        if n1 > n2:
            print(f'O maior número é {n1}')
        if n2 > n1:
            print(f'O maior número é {n2}')
        if n1 == n2:
            print('Os dois valores são iguais!')
    elif escolha == 6:
        n1 = int(input('digite um número:'))
        n2 = int(input('digite outro número:'))
    elif escolha == 7:
        print('finalizando...')
        sleep(2)
        print(emoji.emojize('Volte sempre! :beaming_face_with_smiling_eyes:'))
    else:
        print('opçao invalida... Tente novamente!')
