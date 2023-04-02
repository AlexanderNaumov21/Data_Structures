import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera


fig = plt.figure()
camera = Camera(fig)

index = [0,1,2,3,4, 5,6,7]

array1 = [31,7,21,18,37,3,11,23]
for i in range(0,len(array1)-1): 
    for j in range(len(array1)-1): 
        if(array1[j]>array1[j+1]):

            plt.bar(index, array1, color = 'blue')
            plt.bar(j, array1[j], color = 'red')
            camera.snap() 

            q = array1[j] 
            array1[j] = array1[j+1] 
            array1[j+1] = q 

animation = camera.animate(interval = 1000, repeat = True,
                           repeat_delay = 3000)
 
animation.save('my_animation.gif')


