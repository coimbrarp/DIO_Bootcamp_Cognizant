n = int(input('Insira o valor máximo da sequência: '))

for i in range(n):
    i = i + 1
    while (i > 0) and (i % 2) == 0:
        print(i)
        break