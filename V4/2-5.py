import random
n = 4
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
        K = int(input('Введите K: '))
        break
    except ValueError:
        print("Введено не правильное значение, повторите.")
min_ch = 101
for i in range(n):
    if array_M[i][i] < min_ch:
        min_ch = array_M[i][i]
        klych = i
print("Минимальное число на главной диагонали:", min_ch)
if min_ch<K:
    for i in range(n):
        array_M[klych][i] = array_M[klych][i] + 1

for i in array_M:  
    print(*i)