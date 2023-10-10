N = int(input('digite um numero inteiro:'))
print(''' ESCOLHA UMA DAS BASES DE CONVERSAO:
[1] BINARIO
[2] HEXADECIMAL
[3] OCTAL''')
o = int(input('esolha sua opçao:'))
if o == 1:
    print(f'{N} convertido em BINARIO é {bin(N)[2:]}')
elif o == 2:
    print(f'{N} convertido em HEXADECIMAL é {hex(N)[2:]}')
elif o == 3:
    print(f'{N} convertido em OCTAL é {oct(N)[2:]}')
else:
    print('opçao invalida!')