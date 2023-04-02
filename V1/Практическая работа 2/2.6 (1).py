import random
n, m = -1, -1
# Задаем кол-во строк и столбцов с защитой от дурака
while m<0 or n<0 :
    try:
        m = int(input("Введите кол-во строк:"))
        n = int(input("Введите кол-во столбцов:"))
        if m<1 or n<1:
            print("Должно быть: m>0 и n>0")
        #break
    except ValueError:
        print('Введите ЦЕЛОЕ ЧИСЛО')
K = m*n*2 # задаем для того что бы запустился цикл
# вводим число К с защитой от дурака
while m*n < K or K<1:
    try:
        K = int(input("Введите число K: "))
        #break
    except ValueError:
        print('Введите ЦЕЛОЕ ЧИСЛО')
    if m*n < K:
        print("Должно быть m*n >= K")
    elif K < 1:
        print("Должно быть К>0")
#создаем пустую матрицу
listn = [0]*n 
for i in range(n):
    listn[i] = [0]*m
#Заполняем матрицу нулями и единицами 
chet = 0 # создаем счетчик
# noinspection PyInterpreter
while not(chet == K):
    t = random.randint(0,n-1)
    i = random.randint(0,m-1)
    if listn[t][i] == 0: # создаем защиту от повторений
        listn[t][i] = 1
        chet += 1
#Выводим матрицу в виде таблицы
for t in range(n):
    print(*listn[t])
# меняем нули и единицы на * и пробелы
for t in range(n):
    for i in range(m):
        if listn[t][i] == 0:
            listn[t][i] = " "
        else:
            listn[t][i] = "*"
# выводим матрицу с * и пробелами 
for t in range(n):
    print(*listn[t])

print("+++++++++++++++++++") # просто разделительная линия
listn_revers = [] # создаем доп. список для реверса
for t in range(n): # реверсируем список через цикл
    listn_revers.append(listn[t][::-1])
for t in range(n): # выводим матрицу 4 раза (отраженную во всех областях)
    print(*listn[t], *listn_revers[t])
for t in range(n):
    print(*listn[-(t + 1)], *listn_revers[-(t + 1)])


