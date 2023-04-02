# вариант 15
import random 
n = 22
list_1 = []
list_2 = []
cum = 0
for i in range(n): 
    a = random.randint(-1000, 1000)
    list_1.append(a)

for i in list_1:
    if i < 0 and i%2==1:
        cum += i
        list_2.append(i)
print("Изначальный список:",list_1)
print("Список отрицательных нечетных чисел:",list_2)
print("Сумма отрицательных нечетных чисел:", cum)
