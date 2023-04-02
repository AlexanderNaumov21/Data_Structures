import random
n = -1111
m = -1111

while m<0 or n<0 :
    try:
        n = int(input("Введите количество строк:"))
        m = int(input("Введите количество столбцов:"))
        if m<1 or n<1:
            print("Несовпадает условие: m>0 и n>0")
    except ValueError:
        print('Введите целое число')
K = 10000000000 # задаем для того что бы запустился цикл
# вводим число К с защитой от дурака
while m*n < K or K<1:
    try:
        K = int(input("K это: "))
    except ValueError:
        print('Введите целое число')
    if m*n < K:
        print("Несовпадает условие: m*n >= K")
    elif K < 1:
        print("Несовпадает условие: К>0")
#создаем пустую матрицу
list_m = [0]*n 
for i in range(n):
    list_m[i] = [0]*m
#Заполняем матрицу нулями и единицами 
q = 0 # создаем счетчик

while q != K:
    t = random.randint(0,n-1)
    i = random.randint(0,m-1)
    if list_m[t][i] == 0: # создаем защиту от повторений
        list_m[t][i] = 1
        q += 1

for t in range(n):
    print(*list_m[t])
# меняем нули и единицы на * и пробелы
for t in range(n):
    for i in range(m):
        if list_m[t][i] == 0:
            list_m[t][i] = " "
        else:
            list_m[t][i] = "*"
# выводим матрицу с * и пробелами
print("Изначальная матрица") 
for t in range(n):
    print(*list_m[t])

print("РАЗДЕЛИТЕЛЬНАЯ ПОЛОСА") # просто разделительная линия
# создаем доп. список для реверса
list_m_r = [0]*n 
for i in range(n):
    list_m_r[i] = [0]*m

for t in range(n):
    for i in range(m):
        list_m_r[t][i] = list_m[t][m - i - 1]

for t in range(n): # выводим матрицу 4 раза (отраженную во всех областях)
    print(*list_m[t], *list_m_r[t])
for t in range(n):
    print(*list_m[-(t + 1)], *list_m_r[-(t + 1)])
