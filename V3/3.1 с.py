import random
import math

def bubblesort(arr): 
    for i in range(0,len(arr)-1): 
        for q in range(len(arr)-1): 
            if(arr[q]>arr[q+1]): 
                w = arr[q] 
                arr[q] = arr[q+1] 
                arr[q+1] = w 
    return arr 

def insertionsort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        q = i-1
        while q >=0 and k < arr[q] :
            arr[q+1] = arr[q]
            q -= 1
        arr[q+1] = k
    return arr

def selectionsort(arr):
    n = len(arr)
    for i in range(n - 1):
        mininarr = i
        for q in range(i + 1, n):
            if(arr[q] < arr[mininarr]):
                mininarr = q
        arr[i], arr[mininarr] = arr[mininarr], arr[i]
    return arr
def sheikersort (arr):
    n = len(arr)
    metka = 0
    for i in range(n):
       mininarr = i
       for q in range(n - 1 - i):
          if arr[q] > arr[q + 1]:
              arr[q], arr[q + 1] = arr[q + 1], arr[q]
              metka = 1
          if arr[q] < arr[mininarr]:
              mininarr = q
       if metka == 0:
          break
       if mininarr != i:
          arr[mininarr], arr[i] = arr[i], arr[mininarr]
    return arr

def shellSort(arr):
    n = len(arr)
    p = int(math.log2(n))
    e = 2**p -1
    while e > 0:
        for i in range(e, n):
            t = arr[i]
            q = i
            while q >= e and arr[q - e] > t:
                arr[q] = arr[q - e]
                q -= e
            arr[q] = t
        p -= 1
        e = 2**p -1
    return arr


def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        t = random.choice(arr)
        arr2 = []
        arr3 = []
        arr4 = []
        for e in arr:
            if e < t:
                arr2.append(e) 
            elif e > t: 
                arr4.append(e) 
            else: 
                arr3.append(e)
        return QuickSort(arr2) + arr3 + QuickSort(arr4)

arr = []
for i in range(10):
    x = random.randint(-100, 100)
    arr.append(x)
print("Изначальный массив - ", arr)
print("Пузырьковая сортировка - ",bubblesort(arr))
print("Включением сортировка - ",insertionsort(arr))
print("Выбором сортировка - ",selectionsort(arr))
print("Шейкерная  сортировка - ",sheikersort(arr))
print("Шелла сортировка - ",shellSort(arr))
print("Быстрая сортировка - ",QuickSort(arr))