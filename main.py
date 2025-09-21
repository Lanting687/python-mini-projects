import matplotlib.pyplot as plt
import numpy as np
from utils import generate_random_number
result=generate_random_number(50,1000)
print(result)

arr = np.array([1, 2, 3, 4, 5])
New_arr=arr+1
print(New_arr)

list=[1,2,3,4,5]
New_list=[x+1 for x in list]
#for x in list:
   #New_list.append(x+1)
print(New_list)