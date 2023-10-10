P = float(input('DIGITE SEU PESO:'))
A = float(input('DIGITE SUA ALTURA:'))
IMC = P / (A*A)
print(IMC)
if IMC <= 18.5:
    print(f'seu imc é de {IMC:.2f} voce esta ABAIXO DO PESO!')
elif IMC <= 25:
    print(F'Seu IMC é de {IMC:.2f} voce está no PESO IDEAL!')
elif IMC <= 30:
    print(F'Seu IMC é de {IMC:.2f} voce está SOBREPESO!')
elif IMC <= 40:
    print(F'Seu IMC é de {IMC:.2f} voce está OBESO!')
elif IMC > 40:
    print(F'Seu IMC é de {IMC:.2f} voce tem OBESIDADE MORBITA!')
