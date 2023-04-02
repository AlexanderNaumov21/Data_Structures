import timeit
import math
import matplotlib.pyplot as plt 
import random


def bubble_sort(list_1): 
    for i in range(0,len(list_1)-1): 
        for j in range(len(list_1)-1): 
            if(list_1[j]>list_1[j+1]): 
                tp = list_1[j] 
                list_1[j] = list_1[j+1] 
                list_1[j+1] = tp 
    return list_1 
"""
dfdgfdgjdngfjdflgjfdgjjfgjkdfk
"""
def insertion_sort(list_1):
    for i in range(1, len(list_1)):
        k = list_1[i]
        j = i-1
        while j >=0 and k < list_1[j] :
            list_1[j+1] = list_1[j]
            j -= 1
        list_1[j+1] = k

def selection_sort(list_1):
    n = len(list_1)
    for i in range(n - 1):
        min_ = i
        for j in range(i + 1, n):
            if(list_1[j] < list_1[min_]):
                min_ = j
        list_1[i], list_1[min_] = list_1[min_], list_1[i]

def sheiker_sort (list_1):
    n = len(list_1)
    fl = 0
    for i in range(n):
       min_ = i
       for j in range(n - 1 - i):
          if list_1[j] > list_1[j + 1]:
              list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
              fl = 1
          if list_1[j] < list_1[min_]:
              min_ = j
       if fl == 0:
          break
       if min_ != i:
          list_1[min_], list_1[i] = list_1[i], list_1[min_]

def shellSort(list_1):
    n = len(list_1)
    k = int(math.log2(n))
    inte = 2**k -1
    while inte > 0:
        for i in range(inte, n):
            t = list_1[i]
            j = i
            while j >= inte and list_1[j - inte] > t:
                list_1[j] = list_1[j - inte]
                j -= inte
            list_1[j] = t
        k -= 1
        inte = 2**k -1
    return list_1


def QuickSort(list_1):
    if len(list_1) <= 1:
        return list_1
    else:
        t = random.choice(list_1)
        list_2 = []
        list_3 = []
        list_4 = []
        for element in list_1:
            if element < t:
                list_2.append(element) 
            elif element > t: 
                list_4.append(element) 
            else: 
                list_3.append(element)
        return QuickSort(list_2) + list_3 + QuickSort(list_4)


def chek_time(sort_metod):                                                              # задаем метод вызова сортировок и подсчета времени 
    list_1 = [50, 100, 300, 500, 800, 1200, 1600, 2000, 3000, 5000, 8000, 12000, 20000]
    chek_time_end = []                                                                  # создаем список 1)с кольчеством элементов в списке 2) пустой для ввода времени 
    list_r = []                                                                         # 3) список для заполнения его рандомными числоми в нужном нам количестве
    for n in list_1:
        list_r.append(random.randint(0,100))                                            # заполняем список
        start_time = timeit.default_timer()                                             # запускам время
        for n in range(15):                                                             # каждую итерацию проводим 15 раз для более точного вчисления срееднего времени
            sort_metod(list_r) 
        end_time = timeit.default_timer()                                               # останавливаем время
        time_end = (end_time - start_time)/15                                           # вчисляем среднне время
        chek_time_end.append(time_end)                                                  # полученное время заносим в список

    return chek_time_end                                                                # возращаем список


list_4isla = [50, 100, 300, 500, 800, 1200, 1600, 2000, 3000, 5000, 8000, 12000, 20000]
list_sort = [bubble_sort,insertion_sort,selection_sort,sheiker_sort,shellSort,QuickSort] 
list_sort1 = ["bubble_sort","insertion_sort","selection_sort","sheiker_sort","shellSort","QuickSort"]
for i in range(6):
    plt.plot(list_4isla, chek_time(list_sort[i]), label = list_sort1[i])
plt.xlabel('Кол-во элементов в списке')
plt.ylabel('Время') 
plt.title('Зависимость времени от кол-во элементов в списке')
plt.legend(loc='best')
plt.show()
# 104 создаем легенд на графике
# 106 and 1o7 задаем лейбл оси
# 1o8 задаем название графика
# 11o запускаем график