def linear_Search(list_1, k): 
    nal = []
    c = 0
    n = len(list_1)
    for i in range(0, n): 
        if list_1[i] == k:
            nal.append(i)
            c += 1     
    if c == 0:
        print("Слово не найдено")
    else:
        print("Слово найдено","\n Индексы:", nal, "\nКоличество элементов: ", c)


n = input("Введите текст в котором нужно искать:")
list_1 = [] 
list_1.append(n)
list_1 = list_1[0].split(" ")  
i = input("Что будем искать:")

rezylt = linear_Search(list_1, i) # вызваем функцию поиска
