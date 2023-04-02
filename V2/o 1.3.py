list_1 = [] 
pov_max = 0
pov_min = 0
list_2 = []
while 4 != len(list_1): 
    try: 
        x = int(input("Введите целое число: ")) 
        list_1.append(x)
    except ValueError:
        print("Введено, не целочисленное значение.") 

max_ = list_1[0]
for i in list_1:
    if i > max_:
        max_ = i
min_ = list_1[0]
for i in list_1:
    if i < min_:
        min_ = i
for i in list_1:
    if i == max_:
        pov_max += 1
for i in list_1:
    if i == min_:
        pov_min += 1
print("Максимальное число:",max_,"\nКол-во максимальных чисел:",pov_max,"\nМинимальное число:",min_,"\nКол-во минимальных чисел:",pov_min)