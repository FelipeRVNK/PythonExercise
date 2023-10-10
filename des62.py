'''primeiro = int(input('Primeiro Termo:'))
razao = int(input('Razao:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostar mais?'))
print(f'A progressao foi finalizada com {total} termos mostrados!')'''
primeiro = int(input('primeiro termo:'))
razao = int(input('razao:'))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{primeiro} -', end=' ')
        primeiro += razao
        cont += 1
    mais = int(input('quantos mais?'))
print(f'Progreçao finalizada... Ao todo foram {total} termos mostrados!')
