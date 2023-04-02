i = input("Введите текст - ")
arr = []
arr.append(i)
arr = arr[0].split(" ") # дробим по пробелу 
k = input("Введите искомое слово - ") 

arr_i = []
metka = 0
q = len(arr)
for i in range(0, q): 
    if arr[i] == k:     
        metka = f"Элемент '{k}' есть в списке"
        arr_i.append(i)
if metka == 0:
    print("В массиве нет этого числа - ", k)
else:
    print(metka, "Индексы - ", arr_i)

