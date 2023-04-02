import random
n, m = -1, -1
# Задаем кол-во строк и столбцов  сзащитой от дурака
while m<0 or n<0 or not(n == m) :
    try:
        m = int(input("Введите кол-во строк:"))
        n = int(input("Введите кол-во столбцов:"))
        if m<1 or n<1:
            print("Должно быть: m>0 и n>0")
        elif m != n: # соблюдаем условие "квадраности матрицы"
            print("Кол-во строк и столбцов должно быть одинаковым.")
        
    except ValueError:
        print('Введите ЦЕЛОЕ ЧИСЛО')
K = 0
# задаем К с защитой от дурака
while K<1:
    try:
        K = int(input("Введите число K: "))
        #break
    except ValueError:
        print('Введите ЦЕЛОЕ ЧИСЛО')
    if K < 1:
        print("Должно быть К>0")
#создаем пустую матрицу
listn = [0]*n 
for i in range(n):
    listn[i] = [0]*m
#Заполняем матрицу
for t in range(n):
    for i in range(m):
        listn[t][i]=random.randint(-10,10) 
#Выводим матрицу в виде таблицы
for t in range(n):
    print(*listn[t], sep=' | ')
    print("-----"*m)
listX = [] # задаем доп список для вывода
for t in range(n): # перебираем всю матрицу по элементам
    for i in range(m):
        if t>i and listn[t][i] <= K and listn[t][i]>(t+i) : # пропроверяем по условиям, подходит ли нам число
            listX.append(listn[t][i])
print("Составленный массив Х: ",listX)
