def bubble_sort(array): 
    for i in range(0,len(array)-1): 
        for p in range(len(array)-1): 
            if(array[p]>array[p+1]): 
                y = array[p] 
                array[p] = array[p+1] 
                array[p+1] = y 
    return array 

array1 = []
klych = 0
array2 = []

while True: 
    try: 
        for i in range(4):
            p = int(input("Введите число:"))
            if p in array1:
                klych = klych + 1
            array1.append(p)
        break
    except ValueError:
        print("Это не целые числа, повторите операцию с самого начала.")
        array1 = []
        klych = 0
print("Получившийся список:", array1)

array1  = bubble_sort(array1)

for i in array1: 
    if i not in array2:
        array2.append(i)

if len(array2) < 3:
    print("Третье по велечине число не найдено.") 
elif len(array2) == 3:
    print("Третье по величене число:",array1[3])
else:
    print("Третьего по величене число:",array2[2])