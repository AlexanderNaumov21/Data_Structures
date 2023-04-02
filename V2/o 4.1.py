import random
def linear_Search(list_1, k): 
    n = len(list_1) 
    nal = 0
    for i in range(0, n):
        if list_1[i] == k:
            nal = "Элемент есть в списке"
    return nal

k = -1 #какое число искать
len_1 = 99 #сколько чисел в списке
list_1 = [] 
for i in range(len_1):
            t = random.randint(-100, 100)
            list_1.append(t)
print('Входной список: ', list_1)


 
rezylt = linear_Search(list_1, k) 
if rezylt == 0:
    print("Элемента не существует") 
else: 
    print( rezylt) 
