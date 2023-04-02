import random
n, m = 0, 1
# Задаем кол-во строк и столбцов
# вводим данныые с защитой от дурака
while m<0 or n<0 or not(n == m) :
    try:
        m = int(input("Введите кол-во строк:"))
        n = int(input("Введите кол-во столбцов:"))
        if m<1 or n<1:
            print("Должно быть: m>0 и n>0")
        elif m != n:
            print("Кол-во строк и столбцов должно быть одинаковым.")
    except ValueError:
        print('Введите ЦЕЛОЕ ЧИСЛО')
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
sum_glav = 0 # сумма чисел главной диагонали
for t in range(n): # перебираем главную диагональ по индексу и складываем сумму
    if listn[t][t] > 0:
        sum_glav += listn[t][t]
print ("Сумма положительных чисел главной диагонали:",sum_glav)
sum_poboch = 0 # сумма чисел побочной диагонали
for t in range(n): # перебираем побочную диагональ по индексу и складываем сумму
    sum_poboch += listn[t][n-1-t]
print ("Сумма  чисел побочной диагонали:",sum_poboch)