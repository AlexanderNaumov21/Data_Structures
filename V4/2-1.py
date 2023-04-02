while True:
    try:
        len_arr = int(input('Введите желаемую длину списка: '))
        break
    except ValueError:
        print("Введено не правильное значение, повторите.")

array1 = []

for i in range(len_arr):
    a = input("Введите ваш элемент:")
    array1.append(a)
print("Массив:",array1)

def Reverc(array1):
    array2 = []
    for i in range(1, len(array1)+1):
        array2.append(array1[-i])
    return array2

print("Реверсиванный массив:",Reverc(array1))