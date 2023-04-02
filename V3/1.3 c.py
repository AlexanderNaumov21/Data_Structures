arr1 = []
while not(4 == len(arr1)): 
    try: 
        ch = int(input("Введите число - "))
        arr1.append(ch)
    except ValueError:
        print("Введено число не правильного формата") 
povtorimax = 0
povtorimin = 0
maximym = arr1[0]
minimym = arr1[0]
for i in arr1:
    if i > maximym:
        maximym = i
for i in arr1:
    if i < minimym:
        minimym = i
for i in arr1:
    if i == maximym:
        povtorimax += 1
for i in arr1:
    if i == minimym:
        povtorimin += 1
print("Число максимума - ",maximym)
print("Количество максимумов - ",povtorimax)
print("Число минимума - ",minimym)
print("Количество минимумов -", povtorimin)