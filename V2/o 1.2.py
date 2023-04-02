
list_1 = [] 
pov = 0
list_2 = []
while 4 != len(list_1): 
    try: 
        x = int(input("Введите целое число: "))
        if x in list_1:
            pov += 1 
        list_1.append(x)
    except ValueError:
        print("Введено, не целочисленное значение.") 
for i in list_1:
        if i not in list_2:
            list_2.append(i)
if pov >= 2:
    print("Третьего числа нет")
else:
    print("Третье число:", list_2[2])


