n = "Нет повторяющихся чисел" #Задаем то что изначально нет повторяющихся чисел
list4 = [] #Вводим пустой список
while not(4 == len(list4)): # через цикл вайл добиваемся того что в списке будет 4 числа, пока не наберем 4 - цикл не закончится
    try: # используем конструкцию тру эксепт, если не возникает ошибок то исполняется под "тру", если есть ошибки то под "эксепт"
        x = int(input("Введите целое число: "))#вводим число от пользователя, если оно не в типе "int" то алгаритм переходит к эксепт
        if x in list4: # если находим введенное пользователем число в списке, то сообщаем об этом в переменную "n"
            n = "Есть повторяющееся числа"
        list4.append(x) # добавляем введенную переменную пользавателем в список
    except ValueError:
        print("Введено, не целочисленное значение.") # это вводится при появление ошибки
print("Введенные числа: ", list4) #выводим числа нашего списка
print(n) # сообщаем об наличии/не наличии повторений
