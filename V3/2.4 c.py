# VARIANT 9
import random
# Создаем маccbd Х 4 на 1
matr_X = []
for i in range(4): 
            x = random.randint(-10, 10)
            matr_X.append(x)
print("Изначальный массив X -", '\n',*matr_X)
# Создаем матрицу А 4 на 3
m = 4
n = 3
matr_A = [0]*n
for i in range(n):
    matr_A[i] = [0]*m 
for t in range(n):
    for i in range(m):
        matr_A[t][i]=random.randint(-10,10) 
print("Изначальная матрица A - ")
for t in range(n):
    print(*matr_A[t])
# Вычисляем матрицу У
matr_Y = []
metka = 0
for i in range(3):
    for x in range(len(matr_X)):
        metka += matr_X[x]*int(matr_A[i][x])
    matr_Y.append(metka)
    metka = 0
print("Получившийся массив У - ",*matr_Y)
