import random
array1 = []
array2 = [] 
while True:
    try:
        n = int(input("Введите желаемую длину списка:"))
        k = int(input("Введите число которое хотите найти:"))
        break
    except ValueError:
        print("Неверное число, попробуйте снова.")

for i in range(n): 
    array1.append(random.randint(-100, 100))
print("Наш рандомно заполненный список:",array1)
for i in range(n): 
    if array1[i] == k:
        array2.append(i)
print("Число ",k," имеет индексы:", *array2)
