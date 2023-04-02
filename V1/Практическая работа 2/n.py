import random
def linear_Search(list1, key): 
    n = len(list1)
    list_key = []
    for i in range(0, n): 
        if (list1[i] == key):
            list_key.append(i)      
    return list_key
list1 = []
while len(list1) == 0 :
    try:
        len1 = int(input('Введите длину списка: '))
        key = int(input('Введите искомое число: '))
        for i in range(len1):
            a = random.randint(-10, 10)
            list1.append(a)
    except ValueError:
        print('Введите ЦЕЛОЕ ЧИСЛО')
print('Входной список: ', list1)


 
 
res = linear_Search(list1, key) 
if len(res) == 0: 
    print("Элемента не существует") 
else: 
    print("Индекс(ы) элемента(ов): ", res) 
