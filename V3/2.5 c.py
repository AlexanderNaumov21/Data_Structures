# VARIANT 9
import random
m = 6
n = 6
matr = [0]*n 
for i in range(n):
    matr[i] = [0]*m
for t in range(n):
    for i in range(m):
        matr[t][i]=random.randint(-10,10) 
for t in range(n):
    print(*matr[t])

metka = 0
metka2 = 0
proizv = 1
# пeребираем всю мaтрицу пo элeментам
for t in range(n): 
    for i in range(m):
        if matr[i][t] != 0:
            if t >= i:
                proizv *= matr[i][t]
        elif matr[i][t] == 0 and t >= i:
            metka2 += 1
        else:
            metka += 1
print("Произведение чисел главной диагонали и выше - ",proizv)
print("Количество нулей во всей матрице - ",metka)
print("Количество нулей в матрице в главной диагонали и выше - ",metka2)