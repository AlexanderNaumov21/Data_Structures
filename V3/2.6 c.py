import random
n = -1
m = -1
while m < 0 or n < 0 :
    try:
        n = int(input("Введите кол-во строк в матрице - "))
        m = int(input("Введите кол-во столбцов в матрице - "))
        if m < 1 or n < 1:
            print("По условию должно быть - m > 0 и n > 0")
    except ValueError:
        print('Введено некоректное число')
K = 11111 
while m*n < K or K < 1:
    try:
        K = int(input("Введите К - "))
    except ValueError:
        print('Введено некоректное число')
    if m * n < K:
        print("По условию должно быть - m * n >= K")
    elif K < 1:
        print("По условию должно быть - К > 0")

matr = [0]*n 
for i in range(n):
    matr[i] = [0]*m
metka = 0 

while metka != K:
    e = random.randint(0,n-1)
    i = random.randint(0,m-1)
    if matr[e][i] == 0: 
        matr[e][i] = 1
        metka += 1

for t in range(n):
    print(*matr[t])

for e in range(n):
    for i in range(m):
        if matr[e][i] == 0:
            matr[e][i] = " "
        else:
            matr[e][i] = "*"

print("Начальная матрица -") 
for t in range(n):
    print(*matr[t])

print("Матрица отраженная во всех плоскостях - ") 
matr_revers = [0]*n 
for i in range(n):
    matr_revers[i] = [0]*m

for t in range(n):
    for i in range(m):
        matr_revers[t][i] = matr[t][m - i - 1]

for t in range(n): 
    print(*matr[t], *matr_revers[t])
for t in range(n):
    print(*matr[-(t + 1)], *matr_revers[-(t + 1)])
