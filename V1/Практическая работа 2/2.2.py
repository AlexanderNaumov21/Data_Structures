#Вариант 3, по списку 18
import random
list1 = []
# вводим данные с защитой от дурака 
while len(list1) == 0 :
    try:
        len1 = int(input('Введите длину списка: '))
        for i in range(len1): # рандомом заполняем список
            a = random.randint(-10, 10)
            list1.append(a)
    except ValueError:
        print('Введите ЦЕЛОЕ ЧИСЛО')
print('Входной список: ', list1)
list2 = []
for i in list1: # записываем в новый список квадраты чисел из рандомно заполненного списка
	list2.append(i**2)
print("Выходной список: ",list2)