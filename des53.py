frase = str(input('Digite uma frase:')).strip().replace(" ", "").upper()
print(f'A sua frase {frase}, ao contrario fica {frase[::-1]}!')
if frase == frase[::-1]:
    print('Sua frase é palindromo!')
else:
    print('Sua frase não é um palindromo!')

