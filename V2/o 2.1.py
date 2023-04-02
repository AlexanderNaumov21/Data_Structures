import random
list_1 = []
# вводим данные с защитой от дурака
while len(list_1) == 0:
    try:
        len_1 = int(input('Введите длину списка: '))
        for i in range(len_1): # заполняем список рандомом
            a = random.randint(-1000, 1000)
            list_1.append(a)
    except ValueError:
        print("Введите целое число.")
print('Входной список: ', list_1)
list_r = []

for i in range(len_1):
    list_r.append(list_1[len_1 - i - 1])
print('Выходной список: ', list_r)
