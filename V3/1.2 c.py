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

for i in arr:
    if i not in arr2:
        arr2.append(i)
if povtori >= 2:
    print("Третье число отсутствует")
else:
    print("Третье число - ", arr2[2])
