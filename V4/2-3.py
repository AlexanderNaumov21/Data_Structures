import random
n = 4
m = 3
array_M = [0]*n
print('[0]*n', array_M)
for i in range(n):
    array_M[i] = [0]*m
for j in range(n):   
    for i in range(m):
        array_M[j][i] = random.randint(-3,3)
for i in array_M:  
    print(*i)

klych = 0

for i in range(m):
    if array_M[2][i] > -2 and array_M[2][i] < 2:
        
        klych = klych + 1 
print('Количество чисел в третей строчке, которые <2 и >-2:', klych)

