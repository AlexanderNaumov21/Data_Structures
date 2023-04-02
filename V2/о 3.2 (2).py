import os 
import time


list_1 = [2,7,21,-8,33,1,-9,0]
for i in range(0,len(list_1)-1): 
    for j in range(len(list_1)-1): 
        if(list_1[j]>list_1[j+1]):
            print(list_1)
            time.sleep(0.5) 
            os.system('CLS')  
            tp = list_1[j] 
            list_1[j] = list_1[j+1] 
            list_1[j+1] = tp 
print(list_1)
input("Список отсортирован")