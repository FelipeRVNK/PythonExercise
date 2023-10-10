print(f'{" LOJAS FELIPE ":-^40}')
preço = float(input('preço da sua compra:R$'))
print(''' FORMAS DE PAGAMENTOS
[1] A VISTA DINHEIRO
[2] A VISTA CARTAO
[3] 2X NO CARTAO
[4] 3X OU MAIS NO CARTAO
[5] PIX ''')
opçao = int(input('qual a forma de pagamento?'))
if opçao == 1:
    print(f'A sua compra de R${preço} ficou R${preço - (preço * 10/100):.2f}')
    print('OBRIGADO POR COMPRAR VOLTE SEMPRE!')
elif opçao == 2:
    print(f'A sua compra de R${preço} ficou R${preço - (preço * 5/100):.2f}')
    print('OBRIGADO POR COMPRAR VOLTE SEMPRE!')
elif opçao == 3:
    print(f'A sua compra ficou R$ {preço:.2f} com 2 parcelas de R${preço/2}')
    print('OBRIGADO POR COMPRAR VOLTE SEMPRE!')
elif opçao == 4:
    parcelas = int(input('quantas parcelas?'))
    print(f'A sua compra de R${preço} ficou R$ {preço + (preço * 20/100):.2f}')
    print(f'sua compra sera parcelada em {parcelas}x de {(preço + (preço * 20/100)) / parcelas} COM JUROS')
    print('OBRIGADO POR COMPRAR VOLTE SEMPRE!')
elif opçao == 5:
    print(f'A sua compra ficou R$ {preço:.2f}')
    print('OBRIGADO POR COMPRAR VOLTE SEMPRE!')
else:
 print('ESCOLHA UMA DAS OPÇOES ACIMA!')