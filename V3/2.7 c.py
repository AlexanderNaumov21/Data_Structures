arr1 = []
for i in range(65535):
    arr1.append(i)
arr2 = []
K = 8929
for i in range(65535):
    if i != K:
        arr2.append(i)
print("Недостающее число заданное заранее - ", K)
print("Нехватает числа - ", set(arr1) - set(arr2)) 