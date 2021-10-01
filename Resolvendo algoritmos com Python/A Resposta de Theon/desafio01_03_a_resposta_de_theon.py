n = int(input('Insira o número de tentativas: '))
persons = list(map(int,input('Insira as tentativas: ').split()))

if n == 0 or n > 100:
    pass
else:
    minimo = min(persons)
    print(persons.index(minimo) + 1)    # Encontra a menor posição na lista e soma +1 (para pular o índice 0)