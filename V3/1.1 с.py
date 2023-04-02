
arr = []
arr2 = [] 
povtori = 0 
while not(4 == len(arr)): 
    try: 
        ch = int(input("Введите число - "))
        if ch in arr:
            povtori += 1 
        arr.append(ch)
    except ValueError:
        print("Введено число не правильного формата") 

if povtori == 0:
    print("Повторяющихся чисел нет")
else:
    print("Есть повторяющиеся числа")
