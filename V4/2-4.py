import random
n = 5
m = 4
array_M = [0]*n
for i in range(n):
    array_M[i] = [0]*m
for j in range(n):   
    for i in range(m):
        array_M[j][i] = random.randint(-100,100)
for i in array_M:  
    print(*i)
klych = 0 
while True:
    try:
        K1 = int(input('Введите K1: '))
        K2 = int(input('Введите K2: '))
        break
    except ValueError:
        print("Введено не правильное значение, повторите.")

for i in range(n):
    for p in range(m):
        if (array_M[i][p] <= K2 and array_M[i][p] >= K1) or array_M[i][p]> i+p:
            klych = klych + 1
print("Kоличество элементов, удовлет¬воряющих условию K1 <= Aij <= K2 или Aij > i+j:", klych)