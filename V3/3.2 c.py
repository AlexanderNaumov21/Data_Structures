import os 
import time

arr = [3,4,-9,-6,-1,1,5,-9,3,-2,8]
for i in range(1, len(arr)):
    k = arr[i]
    q = i-1
    while q >=0 and k < arr[q] :
        print(arr)
        time.sleep(0.8) 
        os.system('CLS')  
        arr[q+1] = arr[q]
        q -= 1
    arr[q+1] = k
print(arr)
input("Сортировка массива произведена ")