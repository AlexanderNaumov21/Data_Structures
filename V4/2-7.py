import random
array0 = []
array1 = []
for i in range(65536):
    array0.append(i)
for i in range(65536): 
    array1.append(i)
chiclo = random.randint(0, 65536)
array1.remove(array1[chiclo])#Удаление случайного числа

print("Не хватает числа:",set(array0)-set(array1))


print("Рандомно созданное число и удаленное из списка:", chiclo)