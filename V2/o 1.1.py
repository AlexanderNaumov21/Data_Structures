arr = []
arr2 = [] 
while not(4 == len(arr)): 
    try: 
        ch = int(input("Введите число - "))
        arr.append(ch)
    except ValueError:
        print("Введено число не правильного формата - ") 


for i in arr:
    if i not in arr2:
        arr2.append(i)
if len(arr) == len(arr2):
    print("Повторяющихся чисел нет")
else:
    print("Повторяющиеся числа есть")
print("Введенные числа: ", arr) 
