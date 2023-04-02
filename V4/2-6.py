import random
klych = 0
while True:
    try:
        K = int(input('Введите K: '))
        n  = int(input('Введите количество строк: '))
        m  = int(input('Введите количество столбцов: '))
        break
    except ValueError:
        print("Введено не правильное значение, повторите.")
array_M = [0]*n
for i in range(n):
    array_M[i] = [0]*m
while klych != K:
    j, i = random.randint(0,n-1), random.randint(0,m-1)
    if array_M[j][i] == 0: 
        array_M[j][i] = 1
        klych = klych + 1
for i in range(n):
    for p in range(m):
        if array_M[i][p] == 1:
            array_M[i][p] = '*'
        else:
            array_M[i][p] = ' '
for i in array_M:  
    print(*i)
array_M2 = []
print("Отражение:")
for i in range(n): 
    array_M2.append(array_M[i][::-1])
for i in range(n): 
    print(*array_M[i],*array_M2[i])
for i in range(n):
    print(*array_M[-(i+1)],*array_M2[-(i+1)])
