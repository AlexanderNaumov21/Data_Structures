list1 = ["Текст – это несколько предложений, связанных между собой по смыслу и грамматически. Есть и более «сложная» формулировка данного определения. Текст – это последовательное объединение предложений, которое представляет собой смысловую, содержательную и структурную целостность."]
list1 = list1[0].split(" ") # дробим полученный текст, символом для разбивки служит пробел 

def linear_Search(list1, key): # создаем функцию как в первой задачи, только без рандомного заполнения списка
    n = len(list1)
    list_key = []
    for i in range(0, n): 
        if (list1[i] == key):
            list_key.append(i)      
    return list_key

while True : # через тру эксепт на всякий случай защищаемся от ошибок
    try:
        key = input('Введите искомое слово: ')
        break
    except Exception:
        print('Не коректный ввод')


res = linear_Search(list1, key) # вызваем функцию поиска
if len(res) == 0: # если длина полученного списка 0 то вполняется это условие
    print("Элемента не существует") 
else:  # в остальных случаях
    print("Индекс(ы) элемента(ов): ", res) 