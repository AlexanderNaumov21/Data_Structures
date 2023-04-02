array1 = []
klych = 0

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

min_ch = array1[0]
max_ch = array1[0]
col_min_ch = 0
col_max_ch = 0

for i in array1:
    if i > max_ch:
        max_ch = i
    elif i < min_ch:
        min_ch = i 
print("Максимум:", max_ch)
print("Минимум:", min_ch)
for i in array1:
    if i == max_ch:
        col_max_ch = col_max_ch + 1 
    elif i == min_ch:
        col_min_ch = col_min_ch + 1  
print("Количество максимумумов:", col_max_ch)
print("Количество минимумов:", col_min_ch)
