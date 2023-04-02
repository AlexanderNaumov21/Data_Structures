# VARIANT 9
import random
A = []
B = []
AB_sum = ["Сумма"]
AB_raz = ["Разность"]
for i in range(20): 
    x = random.randint(-10, 10)
    A.append(x)
    y = random.randint(-10, 10)
    B.append(y)
print("Изначальные списки - ",A, B)
for i in range(20):
	AB_sum.append(A[i]+B[i])
	AB_raz.append(A[i]-B[i])
for i in range(20):
	print(f'{AB_sum[i]}, {AB_raz[i]}')