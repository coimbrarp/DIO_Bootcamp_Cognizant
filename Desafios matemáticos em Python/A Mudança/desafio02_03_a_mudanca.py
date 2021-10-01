while True:
    try:
        m = int(input('Insira um valor entre 0 e 360: '))
        if (m == 0) or (m == 360) or (0 < m < 90):
            print("Bom Dia!!")
        elif (90 <= m < 180):
            print("Boa Tarde!!")
        elif (180 <= m < 270):
            print("Boa Noite!!")
        elif (270 <= m < 360):
            print("De Madrugada!!")
    except EOFError:
        break