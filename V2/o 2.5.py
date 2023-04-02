import random
m = 6
n = 6
K = 0
while K<1:
    try:
        K = int(input("'K' это: "))
    except ValueError:
        print('Введите целое число')
    if K < 1:
        print("К должен быть больше 0")
list_m = [0]*n 
for i in range(n):
    list_m[i] = [0]*m

for t in range(n):
    for i in range(m):
        list_m[t][i]=random.randint(-100,100) 
        
for t in range(n):
    print(*list_m[t])


list_Y = [] # задаем доп список для вывода
for t in range(n): # перебираем всю матрицу по элементам
    for i in range(m):
        if list_m[t][i] <= K and list_m[t][i]>(t+i) and t+i<=m-1: # пропроверяем по условиям, подходит ли нам число
            list_Y.append(list_m[t][i])
print("Mассив Y: ",list_Y)
