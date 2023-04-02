import random
list1 = []
# вводим данные с защитой от дурака
while len(list1) == 0:
    try:
        len1 = int(input('Введите длину списка: '))
        for i in range(len1): # заполняем список рандомом
            a = random.randint(-100, 100)
            list1.append(a)
    except ValueError:
        print('Введите ЦЕЛОЕ ЧИСЛО')
print('Входной список: ', list1)
len_round = round(len1//2) # делим длину списка без остатка чтобы вычислить кол-во итераций по смене элементов

for i in range(len_round): # реверсом меняем элементы по индексу 
    list1[0+i],list1[len1-1-i], = list1[len1-1-i],list1[0+i] 
print('Выходной список: ', list1)
