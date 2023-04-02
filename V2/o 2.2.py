# вариант 15
import random 
n = 15 # количество переменных в списке
list_1 = []
list_2 = []
for i in range(n): 
    a = random.randint(-1000, 1000)
    list_1.append(a)

for i in list_1:
    if i < 0:
        list_2.append(i)

max_ = list_2[0]
for i in list_2:
    if i > max_:
        max_ = i
print("Изначальный список:", list_1)
print("Наибольшее из отрицательных:", max_)