import random
q = 7 #искомое число
dlina = 50 #количество чисел в массиве
arr = [] 
for i in range(dlina):
    e = random.randint(-10, 10)
    arr.append(e)
print('Рандомно созданный массив - ', *arr)

arr_i = []
r = len(arr) 
metka = 0
for i in range(0, r):
    if arr[i] == q:
        metka = f"Элемент {q} есть в списке"
        arr_i.append(i)
if metka == 0:
    print("В массиве нет этого числа - ", q)
else:
    print(metka, "Индексы - ", arr_i)