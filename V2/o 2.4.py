import random
m = 7
n = 3
list_m = [0]*n
#print(list_m,"5") 
for i in range(n):
    list_m[i] = [0]*m
#print(list_m,"6,7") 
for t in range(n):
    for i in range(m):
        list_m[t][i]=random.randint(-10,10) 
print("Изначальная матрица:")
for t in range(n):
    print(*list_m[t])

for i in range(3):
    for x in range(n):
        list_m[i][x] = 2
print("Новая матрица:")
for t in range(n):
    print(*list_m[t])

