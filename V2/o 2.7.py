K = 44
list_1 = []
list_2 = []
for i in range(65535):
    list_1.append(i)
for i in range(65535):
    if i != K:
        list_2.append(i)

list_3 = list(set(list_1) - set(list_2)) # находим разницу между наборами этих списков

print("Нехватает числа:", list_3) 