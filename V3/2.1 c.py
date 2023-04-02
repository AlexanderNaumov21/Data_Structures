import random
arr1 = []
revers_arr = []
while not(len(arr1) != 0):
    try:
        dln_arr = int(input('Желаемая длина массива - '))
        for i in range(dln_arr): 
            x = random.randint(-10, 10)
            arr1.append(x)
    except ValueError:
        print("Введен не правильный формат числа")
for i in range(dln_arr):
    revers_arr.append(arr1[dln_arr - i - 1])
print('Массив изначальный - ', arr1)
print('Массив реверсированный - ', revers_arr)
