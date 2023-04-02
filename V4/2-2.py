import random
# вариает 4
array_x = []
array_x_pol = []
array_x_otr = []
for i in range(16):
	p = random.randint(-100, 100)
	array_x.append(p)
print("Наш массив:", array_x)
for i in array_x:
	if i > -1:
		array_x_pol.append(i)
	else:
		array_x_otr.append(i)
print("Положительные числа массива:", array_x_pol)
print("Отрицательные числа массива:", array_x_otr)