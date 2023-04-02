import matplotlib.pyplot as plt 
import time 
import random
import math
import timeit

def bubble_sort(nums): # создаем функцию сортировки пузырьком
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped: 
        swapped = False
        for i in range(len(nums) - 1):# перебираем список
            if nums[i] > nums[i + 1]: # если выбранное число больше соседнего то меняем элементы местами
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert
def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
"""Создадим функцию selection_sort, которая принимает на вход список.
Внутри функции создадим цикл с переменной i, которая будет исчисляться с 0 до (длины списка - 1)
Создадим переменную smallest = i.
Создадим внутренний цикл с переменной j от i + 1 до (длины списка - 1).
Внутри этого цикла, если j-элемент (элемент под индексом j) меньше, чем элемент с индексом smallest, тогда устанавливаем smallest = j.
После завершения внутреннего цикла меняем местами элементы под индексами i и smallest."""
def sheiker_sort (ls):
    n = len(ls)
    flag = 0
    for i in range(n):
       min = i
       for j in range(n - 1 - i):
          if ls[j] > ls[j + 1]:
              ls[j], ls[j + 1] = ls[j + 1], ls[j]
              flag = 1
          if ls[j] < ls[min]:
              min = j
       if flag == 0:
          break
       if min != i:
          ls[min], ls[i] = ls[i], ls[min]
"""Данный тип сортировки представляет собой улучшенный вариант пузырькового способа упорядочивания данных.
 Он является двунаправленным и потому еще называется метод сортировки коктейлем. Принцип данного способа состоит в том,
  что мы делаем проход сначала в одну сторону массива, сравнивая и сортируя по очереди соседние два числа массива.
   Когда мы дошли до конца массива, наиболее крупное число оказывается в правой его части."""
def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array
"""Идея метода заключается в сравнение разделенных на группы элементов последовательности, находящихся друг от друга на некотором 
расстоянии. Изначально это расстояние равно d или N/2, где N — общее число элементов. На первом шаге каждая группа включает в себя
 два элемента расположенных друг от друга на расстоянии N/2; они сравниваются между собой, и, в случае необходимости, 
 меняются местами. На последующих шагах также происходят проверка и обмен, но расстояние d сокращается на d/2, и количество групп,
соответственно, уменьшается. Постепенно расстояние между элементами уменьшается, и на d=1 проход по массиву происходит в последний раз."""
def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem) 
            elif elem > q: 
                R.append(elem) 
            else: 
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)
"""Суть сортировки:
Выбрать опорный элемент из массива. Обычно опорным элементом является средний элемент.
Разделить массив на два подмассива: элементы меньше опорного и элементы больше опорного.
Рекурсивно применить сортировку к двум подмассивам."""
def time_counter(sort_metod):# задаем метод вызова сортировок и подсчета времени 
    list1 = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 2000, 2500, 3000, 4000, 5000]
    time_finish_list = [] # создаем список 1)с кольчеством элементов в списке 2) пустой для ввода времени 
    list_random = [] # 3) список для заполнения его рандомными числоми в нужном нам количестве
    for n in list1:
        list_random.append(random.randint(0,100)) # заполняем список
        start_time = timeit.default_timer() # запускам время
        for n in range(15): # каждую итерацию проводим 15 раз для более точного вчисления срееднего времени
            sort_metod(list_random) 
        end_time = timeit.default_timer() # останавливаем время
        time_finish = (end_time - start_time)/15 # вчисляем среднне время
        time_finish_list.append(time_finish) # полученное время заносим в список

    return time_finish_list # возращаем список

#print(time_counter(QuickSort))
list_4isla = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 2000, 2500, 3000, 4000, 5000]
list_sort = [bubble_sort,insertion_sort,selection_sort,sheiker_sort,shellSort,QuickSort] 
# списки (list_sort,list_sort1) наших сортировок, нужен для графического отображения
list_sort1 = ["bubble_sort","insertion_sort","selection_sort","sheiker_sort","shellSort","QuickSort"]
for i in range(6): # создаем легенд на графике
    plt.plot(list_4isla, time_counter(list_sort[i]), label = list_sort1[i])
plt.xlabel('Кол-во элементов в списке')  #задаем лейбл оси
plt.ylabel('Время') # задаем лейбл оси
plt.title('Зависимость времени от кол-во элементов в списке') #задаем название графика
plt.legend(loc='best') # вбираем место расположения легенд
plt.show() # запускаем график