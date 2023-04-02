# VARIANT 9
import random
A = []
metka = 0
for i in range(11): 
    x = random.randint(-10, 10)
    A.append(x)

print("Наш массив - ", A)
for i in range(len(A)):
	if A[i] == A[-1]:
		print("Массив отсортирован по убыванию")
		break
	else:
		if not(A[i] >= A[i+1]):
			print("Массив не отсортирован по убыванию")
			break

A = [9,8,7,6,5,4,3,2,1,0,-1]
print("Наш массив - ", A)
for i in range(len(A)):
	if A[i] == A[-1]:
		print("Массив отсортирован по убыванию")
		break
	else:
		if not(A[i] >= A[i+1]):
			print("Массив не отсортирован по убыванию")
			break