n = int(input('Quantidade de testes: '))

for _ in range(n):
    placa = input('Insira a placa no modelo AAA-9999: ').split('-')
    if placa[0].isupper() and len(placa[0]) == 3 and placa[0].isalpha() and len(placa[-1]) == 4 \
            and ' ' not in list(placa[0]) and ' ' not in list(placa[-1]):
        try:
            check = int(placa[-1])
            r = int(placa[1][3])

            if (r == 9) or (r == 0):
                print('SEXTA')
            elif (r == 7) or (r == 8):
                print('QUINTA')
            elif (r == 5) or (r == 6):
                print('QUARTA')
            elif (r == 3) or (r == 4):
                print('TERCA')
            elif (r == 1) or (r == 2):
                print('SEGUNDA')
        except:
            print('FALHA')

    else:
        print('FALHA')