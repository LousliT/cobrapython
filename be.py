'''
Beecrowd: Problema 
01/08/2024
Prof. Gregory --> Louslane Talevi Pontes
'''

pares = [0] * 5
impares = [0] * 5

i_pares = 0
i_impares = 0

for _ in range(15):
    v = int(input())

    if v % 2 == 0:
        pares[i_pares] = v
        i_pares += 1
        if i_pares == 5:
            for i in range(5):
                print("par[{}] = {}".format(i, pares[i]))
            i_pares = 0

    else:
        impares[i_impares] = v
        i_impares += 1
        if i_impares == 5:
            for i in range(5):
                print("impar[{}] = {}".format(i, impares[i]))
            i_impares = 0


if i_impares > 0:
    for i in range(i_impares):
        print("impar[{}] = {}".format(i, impares[i]))

if i_pares > 0:
    for i in range(i_pares):
        print("par[{}] = {}".format(i, pares[i]))


n = int(input())

x = []

valores = input().split()
for valor in valores:
    x.append(int(valor))

menor_v = x[0]
posicao = 0

for i in range(1, n):
    if x[i] <= menor_v:
        menor_v = x[i]
        posicao = i

print("Menor valor: {}".format(menor_v))
print("Posiçao: {}".format(posicao))










n = int(input())

total_s = 0
total_s_saque = 0
total_b = 0
total_s_bloqueio = 0
total_a = 0
total_s_ataque = 0

for _ in range(n):
    nome = input()

    saque, bloqueio, ataque = map(int, input().split())
    total_s += saque
    total_b += bloqueio
    total_a += ataque

    sucesso_saque, sucesso_bloqueio, sucesso_ataque = map(int, input().split())
    total_s_saque += sucesso_saque
    total_s_bloqueio += sucesso_bloqueio
    total_s_ataque += sucesso_ataque

if total_s > 0: 
    percentual_sucesso_saque = (total_s_saque / total_s) * 100 
else: 
    percentual_sucesso_saque = 0

if total_b > 0:
    percentual_sucesso_bloqueio = (total_s_bloqueio / total_b) * 100 
else: 
    percentual_sucesso_bloqueio = 0

if total_a > 0:
    percentual_sucesso_ataque = (total_s_ataque / total_a) * 100 
else: 
    percentual_sucesso_ataque = 0

print("Pontos de Saque: {:.2f} %.".format(percentual_sucesso_saque))
print("Pontos de Bloqueio: {:.2f} %.".format(percentual_sucesso_bloqueio)) 
print("Pontos de Ataque: {:.2f} %.".format(percentual_sucesso_ataque)) 




while True:
    N = int(input())

    if N == 0:
        break

    resultado = []

    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(1)
        resultado.append(tmp)

    valor = 1
    cima = 0
    esq = 0
    baixo = N - 1
    direita = N - 1

    if N % 2 == 0:
        meio = N / 2

    else:
        meio = (N + 1) / 2


    while valor <= meio:
        i = esq
        while i <= direita:
            resultado[cima][i] = valor
            resultado[baixo][i] = valor
            i += 1

        i = (cima + 1)
        while i < baixo:
            resultado[i][esq] = valor
            resultado[i][direita] = valor
            i += 1

        valor += 1
        cima += 1
        baixo -= 1
        esq += 1
        direita -= 1

    for i in range(N):
        tx = ''
        for j in range(N):
            tx += " %3d" % resultado[i][j]
        print(tx[1:])
    print("")












while True:
    n = int(input())

    if n == 0:
        break

    matriz = []

    for i in range(n):
        x = []
        for j in range(n):
            x.append(1)
        matriz.append(x)

    valor = 1
    dist_ls = 0
    dist_ce = 0
    dist_li = n - 1
    dist_cd = n - 1

    if n % 2 == 0:
        e = n / 2

    else:
        e = (n + 1) / 2

    while valor <= e:
        i = dist_ce
        while i <= dist_cd:
            matriz[dist_ls][i] = valor
            matriz[dist_li][i] = valor
            i += 1

        i = (dist_cd + 1)
        while i < dist_li:
            matriz[i][dist_ce] = valor
            matriz[i][dist_cd] = valor
            i += 1

        valor += 1
        dist_ls += 1
        dist_li -= 1
        dist_ce += 1
        dist_cd -= 1

    for i in range(n):
        y = ''
        for j in range(n):
            y += " %3d" % matriz[i][j]
        print(y[1:])
    print("")



while True:
    n = int(input())
    if n == 0:
        break

    matriz = [[0] * n for _ in range(n)]

    for i in range(n):
        valor = 1
        for j in range(n):
            matriz[i][j] = valor
            valor *= 2

    for i in range(1, n):
        for j in range(n):
            matriz[i][j] = matriz[i - 1][j] * 2

    maior_valor = 0
    for linha in matriz:
        for valor in linha:
            if valor > maior_valor:
                maior_valor = valor

    m = len(str(maior_valor))

    for linha in matriz:
        print(" ".join(f"{x:>{m}}" for x in linha))
    print()





matriz = []

op = input()

for i in range(12):
    matriz.append([])
    for j in range(12):
        a = float(input())
        matriz[i].append(a)

soma = 0
cont = 0

for i in range(n):
    for j in range(n - i - 1, n):
        soma += matriz[i][j]
        cont += 1

media = soma / cont if cont > 0 else 0  

if op == 'S':
    print("{:.1f}".format(soma))
elif op == 'M':
    print("{:.1f}".format(media))