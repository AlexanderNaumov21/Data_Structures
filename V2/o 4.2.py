list_1 = ["2. Написать программу на языке высокого уровня (С++, C#, Java), реализующую поиск подстроки в строке."] # где ищем
list_1 = list_1[0].split(" ") # дробим полученный текст, символом для разбивки служит пробел 
k = "языке" # что ищем
def linear_Search(list_1, k): 
    nal = 0
    n = len(list_1)
    for i in range(0, n): 
        if list_1[i] == k:
            nal = "Элемент есть в списке"      
    return nal

rezylt = linear_Search(list_1, k) # вызваем функцию поиска
if rezylt == 0: 
    print("Элемента не существует") 
else:  
    print(rezylt) 