import random
import math

def sheiker (array0):
    n = len(array0)
    ax = 0
    for i in range(n):
       klych = i
       for w in range(n - 1 - i):
          if array0[w] > array0[w + 1]:
              array0[w], array0[w + 1] = array0[w + 1], array0[w]
              ax = 1
          if array0[w] < array0[klych]:
              klych = w
       if ax == 0:
          break
       if klych != i:
          array0[klych], array0[i] = array0[i], array0[klych]
    return array0

def shell(array0):
    n = len(array0)
    z = int(math.log2(n))
    h = 2**z -1
    while h > 0:
        for i in range(h, n):
            t = array0[i]
            w = i
            while w >= h and array0[w - h] > t:
                array0[w] = array0[w - h]
                w -= h
            array0[w] = t
        z -= 1
        h = 2**z -1
    return array0

def selection(array0):
    n = len(array0)
    for i in range(n - 1):
        klych = i
        for w in range(i + 1, n):
            if(array0[w] < array0[klych]):
                klych = w
        array0[i], array0[klych] = array0[klych], array0[i]
    return array0

def bubble(array0): 
    for i in range(0,len(array0)-1): 
        for w in range(len(array0)-1): 
            if(array0[w]>array0[w+1]): 
                w = array0[w] 
                array0[w] = array0[w+1] 
                array0[w+1] = w 
    return array0 

def insertion(array0):
    for i in range(1, len(array0)):
        k = array0[i]
        w = i-1
        while w >=0 and k < array0[w] :
            array0[w+1] = array0[w]
            w -= 1
        array0[w+1] = k
    return array0


def Quick(array0):
    if len(array0) <= 1:
        return array0
    else:
        q = random.choice(array0)
        Z = []
        X = []
        C = []
        for h in array0:
            if h < q:
                Z.append(h) 
            elif h > q: 
                C.append(h) 
            else: 
                X.append(h)
        return Quick(Z) + X + Quick(C)

array0 = []
while True:
    try:
        k = int(input('Введите длину массива: '))
        break
    except ValueError:
        print("Введено не правильное значение, повторите.")

for i in range(k):
    p = random.randint(-100, 100)
    array0.append(p)
print("Изначальный массив : ", array0)

print("Шейкерная   : ",sheiker(array0) ,"\nШелла  : ",shell(array0), "\nВыбором  : ",selection(array0), "\nПузырьковая  : ",bubble(array0), "\nВключением  : ",insertion(array0), "\nВыбором  : ",selection(array0), "\nБыстрая  : ",Quick(array0))