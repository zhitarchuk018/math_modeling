import numpy as np 

a = np.pi/3
b = 30 * (np.pi/180)
h = 100
import lab_3_task1 as lab3 

v = (( (lab3.g) * h * (np.tan(b)**2)/ 2 * (np.cos(a)**2) * (1 - np.tan(b) * np.tan(a))))
print(v)
